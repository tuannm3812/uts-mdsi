"""Deterministic spatial-temporal matching for the active-fire data pilot."""

from datetime import datetime, timedelta, timezone
import math
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


Point = Tuple[float, float]


def _coordinate_points(coordinates):
    if not coordinates:
        return
    if isinstance(coordinates[0], (int, float)):
        yield float(coordinates[0]), float(coordinates[1])
        return
    for part in coordinates:
        yield from _coordinate_points(part)


def geometry_bounds(geometry: Dict) -> Tuple[float, float, float, float]:
    points = list(_coordinate_points(geometry.get("coordinates", [])))
    if not points:
        raise ValueError("Geometry has no coordinates")
    longitudes = [point[0] for point in points]
    latitudes = [point[1] for point in points]
    return min(longitudes), min(latitudes), max(longitudes), max(latitudes)


def prepare_features(features: Iterable[Dict]) -> List[Dict]:
    prepared = []
    for feature in features:
        copy = dict(feature)
        copy["_bbox"] = geometry_bounds(copy["geometry"])
        prepared.append(copy)
    return prepared


def _point_in_bbox(lon: float, lat: float, bbox: Tuple[float, float, float, float]) -> bool:
    return bbox[0] <= lon <= bbox[2] and bbox[1] <= lat <= bbox[3]


def _point_segment_distance_km(point: Point, start: Point, end: Point) -> float:
    lon_scale = 111.320 * math.cos(math.radians(point[1]))
    lat_scale = 110.574
    ax = (start[0] - point[0]) * lon_scale
    ay = (start[1] - point[1]) * lat_scale
    bx = (end[0] - point[0]) * lon_scale
    by = (end[1] - point[1]) * lat_scale
    segment_x = bx - ax
    segment_y = by - ay
    denominator = segment_x * segment_x + segment_y * segment_y
    if denominator == 0:
        return math.hypot(ax, ay)
    projection = max(0.0, min(1.0, -(ax * segment_x + ay * segment_y) / denominator))
    return math.hypot(ax + projection * segment_x, ay + projection * segment_y)


def point_within_geometry_buffer(
    lon: float, lat: float, geometry: Dict, buffer_km: float
) -> bool:
    if point_in_geometry(lon, lat, geometry):
        return True
    point = (float(lon), float(lat))
    minimum = float("inf")
    coordinates = geometry.get("coordinates", [])
    polygons = [coordinates] if geometry.get("type") == "Polygon" else coordinates
    for polygon in polygons:
        for ring in polygon:
            for index in range(len(ring)):
                start = (float(ring[index - 1][0]), float(ring[index - 1][1]))
                end = (float(ring[index][0]), float(ring[index][1]))
                minimum = min(minimum, _point_segment_distance_km(point, start, end))
                if minimum <= buffer_km:
                    return True
    return False


def _point_on_segment(point: Point, start: Point, end: Point, tolerance: float = 1e-10) -> bool:
    px, py = point
    x1, y1 = start
    x2, y2 = end
    cross = (px - x1) * (y2 - y1) - (py - y1) * (x2 - x1)
    if abs(cross) > tolerance:
        return False
    return (
        min(x1, x2) - tolerance <= px <= max(x1, x2) + tolerance
        and min(y1, y2) - tolerance <= py <= max(y1, y2) + tolerance
    )


def _point_in_ring(point: Point, ring: Sequence[Sequence[float]]) -> bool:
    inside = False
    for index in range(len(ring)):
        start = (float(ring[index - 1][0]), float(ring[index - 1][1]))
        end = (float(ring[index][0]), float(ring[index][1]))
        if _point_on_segment(point, start, end):
            return True
        x1, y1 = start
        x2, y2 = end
        crosses = (y1 > point[1]) != (y2 > point[1])
        if crosses:
            intersection_x = (x2 - x1) * (point[1] - y1) / (y2 - y1) + x1
            if point[0] < intersection_x:
                inside = not inside
    return inside


def _point_in_polygon(point: Point, polygon: Sequence[Sequence[Sequence[float]]]) -> bool:
    if not polygon or not _point_in_ring(point, polygon[0]):
        return False
    return not any(_point_in_ring(point, hole) for hole in polygon[1:])


def point_in_geometry(lon: float, lat: float, geometry: Dict) -> bool:
    """Return whether a WGS84 point lies in a GeoJSON Polygon or MultiPolygon."""
    point = (float(lon), float(lat))
    geometry_type = geometry.get("type")
    coordinates = geometry.get("coordinates", [])
    if geometry_type == "Polygon":
        return _point_in_polygon(point, coordinates)
    if geometry_type == "MultiPolygon":
        return any(_point_in_polygon(point, polygon) for polygon in coordinates)
    raise ValueError("Only Polygon and MultiPolygon geometries are supported")


def parse_datetime(value) -> Optional[datetime]:
    if value in (None, ""):
        return None
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value / 1000, tz=timezone.utc)
    text = str(value).strip().replace("Z", "+00:00")
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def within_event_window(observed_at: datetime, properties: Dict, grace_days: int) -> bool:
    """Check an observation against ignition/extinguish dates plus symmetric grace."""
    ignition = parse_datetime(properties.get("ignition_date"))
    if ignition is None:
        return False
    extinguish = parse_datetime(properties.get("extinguish_date")) or ignition
    grace = timedelta(days=grace_days)
    observed = parse_datetime(observed_at)
    return ignition - grace <= observed <= extinguish + grace


def _normalized_fire_type(value: Optional[str]) -> str:
    normalized = (value or "").strip().lower().replace(" ", "_")
    if normalized in {"bushfire", "wildfire", "wild_fire"}:
        return "bushfire"
    if normalized in {"prescribed_burn", "hazard_reduction", "planned_burn"}:
        return "prescribed_burn"
    return "other_fire"


def classify_hotspot(
    hotspot: Dict,
    features: Iterable[Dict],
    grace_days: int = 1,
    spatial_buffer_km: float = 0.0,
) -> Dict:
    """Classify one hotspot using polygon containment and the event date window."""
    observed_at = parse_datetime(hotspot["datetime"])
    spatial_matches: List[Dict] = []
    temporal_matches: List[Dict] = []
    for feature in features:
        if feature.get("_bbox"):
            degree_buffer = spatial_buffer_km / 80.0
            bbox = feature["_bbox"]
            expanded = (
                bbox[0] - degree_buffer,
                bbox[1] - degree_buffer,
                bbox[2] + degree_buffer,
                bbox[3] + degree_buffer,
            )
            if not _point_in_bbox(
                float(hotspot["longitude"]), float(hotspot["latitude"]), expanded
            ):
                continue
        if point_within_geometry_buffer(
            hotspot["longitude"],
            hotspot["latitude"],
            feature["geometry"],
            spatial_buffer_km,
        ):
            spatial_matches.append(feature)
            if within_event_window(observed_at, feature.get("properties", {}), grace_days):
                temporal_matches.append(feature)

    if temporal_matches:
        chosen = sorted(
            temporal_matches,
            key=lambda feature: (
                parse_datetime(feature.get("properties", {}).get("ignition_date"))
                or datetime.max.replace(tzinfo=timezone.utc),
                str(feature.get("properties", {}).get("fire_id") or ""),
            ),
        )[0]
        properties = chosen.get("properties", {})
        return {
            **hotspot,
            "match_class": _normalized_fire_type(properties.get("fire_type")),
            "fire_id": properties.get("fire_id"),
            "fire_name": properties.get("fire_name"),
            "spatial_match_count": len(spatial_matches),
            "temporal_match_count": len(temporal_matches),
        }

    return {
        **hotspot,
        "match_class": "spatial_only" if spatial_matches else "unmatched",
        "fire_id": None,
        "fire_name": None,
        "spatial_match_count": len(spatial_matches),
        "temporal_match_count": 0,
    }
