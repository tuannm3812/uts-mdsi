from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import urllib.parse
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "llm-wiki"
SUBJECTS_ROOT = WIKI / "02-subjects"
MANIFEST_PATH = WIKI / "00-admin" / "drive-import-manifest.csv"
PLANS_ROOT = ROOT / "docs" / "superpowers" / "plans"
AUDIT_ROOT = ROOT / "docs" / "superpowers" / "audit"
CONTRACT_FILE = ROOT / "docs" / "superpowers" / "contracts" / "content-contracts.md"


ALLOWED_MANIFEST_STATUSES = {
    "copied",
    "already-copied",
    "referenced-binary-file",
    "referenced-large-file",
    "missing",
    "duplicate-destination",
    "error",
}


@dataclass(frozen=True)
class Issue:
    severity: str
    rule: str
    file: str
    message: str
    line: int | None = None

    def format(self) -> str:
        location = f"{self.file}:{self.line}" if self.line else self.file
        return f"[{self.severity.upper()}] {location} ({self.rule}) {self.message}"


LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
FM_RE = re.compile(r"^(?P<key>[A-Za-z0-9_-]+):\s*(?P<value>.*)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate llm-wiki content conventions")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when hard errors are found",
    )
    parser.add_argument("--subject", action="append", default=[], help="Limit checks to one or more subject slugs")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Write a JSON audit report into docs/superpowers/audit/",
    )
    parser.add_argument("--no-manifest", action="store_true", help="Skip manifest checks")
    return parser.parse_args()


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text

    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return {}, text

    raw = match.group(1)
    body = text[match.end() :]
    payload: dict[str, str] = {}

    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = FM_RE.match(line)
        if not m:
            continue
        key = m.group("key")
        value = m.group("value").strip()
        if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]
        payload[key] = value
    return payload, body


def add_issue(
    issues: list[Issue],
    severity: str,
    rule: str,
    file: Path,
    message: str,
    line: int | None = None,
) -> None:
    issues.append(Issue(severity=severity, rule=rule, file=str(file), message=message, line=line))


def is_external_link(target: str) -> bool:
    if not target:
        return True
    lowered = target.lower()
    return (
        target.startswith("#")
        or lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("mailto:")
        or lowered.startswith("ftp://")
        or lowered.startswith("obsidian://")
        or lowered.startswith("file://")
    )


def _normalized_target(raw_target: str) -> str:
    target = raw_target.strip()
    if not target:
        return ""
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target:
        target = target.split(" ", 1)[0]
    target = target.split("?", 1)[0]
    target = target.split("#", 1)[0]
    return urllib.parse.unquote(target).strip()


def rel_links(path: Path, md_text: str) -> list[tuple[str, int]]:
    results: list[tuple[str, int]] = []
    for line_no, line in enumerate(md_text.splitlines(), start=1):
        for match in LINK_RE.finditer(line):
            raw_target = match.group(1).strip()
            target = _normalized_target(raw_target)
            if is_external_link(target):
                continue
            if target.startswith("/"):
                # Vault-absolute path can be ambiguous across clients; keep checks conservative.
                continue
            results.append((target, line_no))
    return results


def _file_signature(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), hashlib.sha1(data).hexdigest()


def relpath_exists(source_file: Path, rel: str) -> bool:
    target = (source_file.parent / rel).resolve()
    return target.exists()


def headings(md: str) -> list[str]:
    return [m.group(2).strip().lower() for m in HEADING_RE.finditer(md)]


def check_frontmatter_subject(path: Path, issues: list[Issue]) -> None:
    fm, body = parse_frontmatter(path)
    if not fm:
        add_issue(
            issues,
            "error",
            "frontmatter.missing",
            path,
            "Subject README missing frontmatter (expected type/status).",
        )
        return

    if fm.get("type") != "subject-index":
        add_issue(
            issues,
            "error",
            "frontmatter.subject-type",
            path,
            f"Subject README frontmatter type expected 'subject-index', got {fm.get('type')!r}",
        )
    if fm.get("status") != "active":
        add_issue(
            issues,
            "error",
            "frontmatter.subject-status",
            path,
            f"Subject README frontmatter status expected 'active', got {fm.get('status')!r}",
        )
    if not fm.get("code"):
        add_issue(
            issues,
            "warn",
            "frontmatter.subject-code",
            path,
            "Subject README missing optional code field",
        )

    for req in [
        "folder convention",
        "what this subject is about",
        "source subfolders",
        "key concepts",
        "assessments",
        "curated study layer",
        "import summary",
    ]:
        if req not in headings(body):
            add_issue(
                issues,
                "warn",
                "subject.sections",
                path,
                f"Subject README missing section: {req}",
            )


def check_frontmatter_assessment(path: Path, issues: list[Issue]) -> None:
    fm, body = parse_frontmatter(path)
    if not fm:
        add_issue(issues, "error", "frontmatter.missing", path, "assessment-planning.md missing frontmatter block")
        return

    if fm.get("type") != "assessment":
        add_issue(
            issues,
            "error",
            "frontmatter.assessment-type",
            path,
            f"assessment-planning frontmatter type expected 'assessment', got {fm.get('type')!r}",
        )
    if fm.get("status") != "planning":
        add_issue(
            issues,
            "error",
            "frontmatter.assessment-status",
            path,
            f"assessment-planning frontmatter status expected 'planning', got {fm.get('status')!r}",
        )
    if not fm.get("subject"):
        add_issue(issues, "error", "frontmatter.assessment-subject", path, "assessment-planning missing subject key")
    if not fm.get("code"):
        add_issue(issues, "warn", "frontmatter.assessment-code", path, "assessment-planning missing optional code key")

    # Validate AT links
    links = [(t, ln) for t, ln in rel_links(path, body) if re.match(r"(?i)^at\d+\.md$", Path(t).name)]
    if not links:
        add_issue(issues, "warn", "assessment.at-links", path, "No AT links found in assessment-planning.md")

    for target, line_no in links:
        if not relpath_exists(path, target):
            add_issue(
                issues,
                "error",
                "assessment.at-link-missing",
                path,
                f"AT link target missing: {target}",
                line_no,
            )


def check_assignments_dashboard(path: Path, issues: list[Issue]) -> None:
    _, body = parse_frontmatter(path)
    heading_list = headings(body)
    required = {
        "assessment pages",
        "standard review workflow",
        "llm review prompt",
    }
    for req in sorted(required):
        if req not in heading_list:
            add_issue(
                issues,
                "warn",
                "assignments-dashboard.sections",
                path,
                f"Assignments dashboard missing section: {req}",
            )

    if "source count" not in heading_list and "raw imports" not in heading_list:
        add_issue(
            issues,
            "warn",
            "assignments-dashboard.sections",
            path,
            "Assignments dashboard should include '## Source Count' or '## Raw Imports'",
        )
    if "raw imports" not in heading_list:
        add_issue(
            issues,
            "warn",
            "assignments-dashboard.sections",
            path,
            "Assignments dashboard should include '## Raw Imports' (or keep alias equivalent)",
        )

    for target, line_no in rel_links(path, body):
        if target.endswith(".md") and not relpath_exists(path, target):
            add_issue(
                issues,
                "warn",
                "assignments-dashboard.broken-link",
                path,
                f"Broken local link in assignments README: {target}",
                line_no,
            )


def check_duplicate_raw_basenames(subject_dir: Path, issues: list[Issue]) -> None:
    raw_dirs = [
        ("assignments/raw", subject_dir / "assignments" / "raw"),
        ("sources/raw", subject_dir / "sources" / "raw"),
        ("lectures/raw", subject_dir / "lectures" / "raw"),
        ("notebooks/raw", subject_dir / "notebooks" / "raw"),
    ]

    for label, raw_dir in raw_dirs:
        if not raw_dir.exists():
            continue
        counts: dict[str, list[Path]] = defaultdict(list)
        for path in raw_dir.rglob("*"):
            if path.is_file():
                counts[path.name.lower()].append(path)

        dups = {n: items for n, items in counts.items() if len(items) > 1}
        for name in list(dups):
            items = dups[name]
            signatures = {_file_signature(item) for item in items}
            if len(signatures) == 1:
                del dups[name]

        if dups:
            first = sorted(dups)[:5]
            add_issue(
                issues,
                "warn",
                "raw-duplicates",
                subject_dir / label,
                f"{label} has {len(dups)} duplicate basenames; first examples: {', '.join(first)}",
            )


def check_file_links(path: Path, issues: list[Issue]) -> None:
    _, body = parse_frontmatter(path)
    for target, line_no in rel_links(path, body):
        if not relpath_exists(path, target):
            add_issue(
                issues,
                "warn",
                "markdown.broken-link",
                path,
                f"Broken local link target: {target}",
                line_no,
            )


def check_manifest(issues: list[Issue]) -> None:
    if not MANIFEST_PATH.exists():
        add_issue(issues, "warn", "manifest.missing", MANIFEST_PATH, "drive-import-manifest.csv missing")
        return

    required = {
        "semester",
        "drive_subject",
        "repo_subject",
        "target_bucket",
        "source_file",
        "repo_file",
        "status",
        "bytes_copied",
        "source_checksum",
        "repo_checksum",
    }
    with MANIFEST_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        if columns != required:
            missing = sorted(required - columns)
            extra = sorted(columns - required)
            if missing:
                add_issue(
                    issues,
                    "warn",
                    "manifest.columns",
                    MANIFEST_PATH,
                    f"Manifest missing required columns: {', '.join(missing)}",
                )
            if extra:
                add_issue(
                    issues,
                    "warn",
                    "manifest.columns",
                    MANIFEST_PATH,
                    f"Manifest has unexpected columns: {', '.join(extra)}",
                )

        repo_file_rows: dict[str, list[tuple[int, str]]] = defaultdict(list)
        manifest_subjects = set()

        for line_no, row in enumerate(reader, start=2):
            for col in required:
                if col not in row or not str(row[col]).strip():
                    add_issue(
                        issues,
                        "warn",
                        "manifest.row",
                        MANIFEST_PATH,
                        f"Row {line_no}: missing required value in '{col}'",
                    )

            status = str(row.get("status", "")).strip()
            subject = str(row.get("repo_subject", "")).strip()
            source = str(row.get("source_file", "")).strip()
            repo_file = str(row.get("repo_file", "")).strip()
            if status:
                manifest_subjects.add(subject)
                if status not in ALLOWED_MANIFEST_STATUSES:
                    add_issue(
                        issues,
                        "warn",
                        "manifest.status",
                        MANIFEST_PATH,
                        f"Row {line_no}: unexpected status {status!r}",
                    )
                if status in {"copied", "already-copied"} and repo_file and not Path(repo_file).exists():
                    add_issue(
                        issues,
                        "warn",
                        "manifest.repo-file",
                        MANIFEST_PATH,
                        f"Row {line_no}: copied artifact path not found {repo_file}",
                    )
                if status in {"copied", "already-copied", "referenced-binary-file", "referenced-large-file"} and source:
                    if not Path(source).exists():
                        add_issue(
                            issues,
                            "warn",
                            "manifest.source-file",
                            MANIFEST_PATH,
                            f"Row {line_no}: source path not found {source}",
                        )

            if repo_file:
                repo_file_rows[repo_file].append((line_no, status))

        for subject in sorted((d.name for d in SUBJECTS_ROOT.iterdir() if d.is_dir()), key=str):
            if subject not in manifest_subjects:
                add_issue(
                    issues,
                    "warn",
                    "manifest.subject-gap",
                    MANIFEST_PATH,
                    f"Subject missing from manifest: {subject}",
                )

        for repo_file, rows in repo_file_rows.items():
            if len(rows) > 1:
                locations = ", ".join(str(line_no) for line_no, _ in rows)
                add_issue(
                    issues,
                    "warn",
                    "manifest.duplicate-dest",
                    MANIFEST_PATH,
                    f"Duplicate destination entries for {repo_file}: rows {locations}",
                )


def subject_files_for_checks() -> list[Path]:
    files = []
    for subject in sorted(SUBJECTS_ROOT.iterdir()):
        if not subject.is_dir() or subject.name.startswith("."):
            continue
        files.append(subject / "README.md")
        files.extend(
            subject / bucket / "README.md"
            for bucket in ("assignments", "lectures", "notebooks", "questions", "sources")
        )
    return [path for path in files if path.exists()]


def check_subject(subject_dir: Path, issues: list[Issue]) -> None:
    readme = subject_dir / "README.md"
    if not readme.exists():
        add_issue(
            issues,
            "error",
            "subject.missing-file",
            subject_dir / "README.md",
            "Subject folder missing README.md",
        )
    else:
        check_frontmatter_subject(readme, issues)

    assignments_dir = subject_dir / "assignments"
    if not assignments_dir.exists():
        add_issue(
            issues,
            "error",
            "subject.missing-folder",
            subject_dir / "assignments",
            "Subject missing assignments folder",
        )
    else:
        assignments_readme = assignments_dir / "README.md"
        if not assignments_readme.exists():
            add_issue(
                issues,
                "error",
                "assignments.missing-readme",
                assignments_dir / "README.md",
                "Missing assignments/README.md",
            )
        else:
            check_assignments_dashboard(assignments_readme, issues)

        assessment_planning = assignments_dir / "assessment-planning.md"
        if not assessment_planning.exists():
            add_issue(
                issues,
                "error",
                "assignments.missing-planning",
                assignments_dir / "assessment-planning.md",
                "Missing assignments/assessment-planning.md",
            )
        else:
            check_frontmatter_assessment(assessment_planning, issues)

        for at_file in sorted(assignments_dir.glob("*.md")):
            if at_file.name in {"README.md", "assessment-planning.md", "evidence-map.md"}:
                continue
            if not re.fullmatch(r"at\d+\.md|week-\d{2}\.md|project\.md", at_file.name, re.IGNORECASE):
                if at_file.stem.lower().startswith("assignment"):
                    add_issue(
                        issues,
                        "warn",
                        "assignments.naming",
                        at_file,
                        f"Legacy assignment naming style: {at_file.name}",
                    )
                else:
                    add_issue(
                        issues,
                        "warn",
                        "assignments.naming",
                        at_file,
                        f"Unexpected assignment file name: {at_file.name}",
                    )

    check_duplicate_raw_basenames(subject_dir, issues)
    for md in subject_files_for_checks():
        if md.is_relative_to(subject_dir):
            check_file_links(md, issues)


def filter_subjects(selected: list[str]) -> set[str]:
    if not selected:
        return set()
    return {s.strip() for s in selected if s.strip()}


def check_docs(issues: list[Issue]) -> None:
    docs = [CONTRACT_FILE, WIKI / "README.md"]
    for doc in PLANS_ROOT.glob("*.md"):
        docs.append(doc)
    for doc in docs:
        if doc.exists():
            check_file_links(doc, issues)


def print_and_report(issues: list[Issue], strict: bool, selected: set[str], write_report: bool) -> int:
    error_count = 0
    warn_count = 0
    by_sev: dict[str, list[Issue]] = defaultdict(list)
    for issue in issues:
        by_sev[issue.severity].append(issue)
        if issue.severity == "error":
            error_count += 1
        else:
            warn_count += 1

    for severity in ("error", "warn"):
        entries = by_sev.get(severity, [])
        if not entries:
            continue
        print(f"\n{severity.upper()}S ({len(entries)}):")
        for issue in sorted(entries, key=lambda i: (i.file, i.rule)):
            print(issue.format())

    print(f"\nSummary: {error_count} error(s), {warn_count} warning(s)")

    if write_report:
        AUDIT_ROOT.mkdir(parents=True, exist_ok=True)
        out = AUDIT_ROOT / f"llm-wiki-audit-{datetime.now().strftime('%Y-%m-%d')}.json"
        out.write_text(
            json.dumps(
                {
                    "generated_at": datetime.now().isoformat(timespec="seconds"),
                    "strict": strict,
                    "selected_subjects": sorted(selected),
                    "counts": {"error": error_count, "warning": warn_count, "total": len(issues)},
                    "issues": [
                        {
                            "severity": i.severity,
                            "rule": i.rule,
                            "file": i.file,
                            "line": i.line,
                            "message": i.message,
                        }
                        for i in issues
                    ],
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"Report: {out}")

    if strict and error_count:
        return 1
    return 0


def main() -> int:
    args = parse_args()
    selected = filter_subjects(args.subject)

    issues: list[Issue] = []
    for subject in sorted(SUBJECTS_ROOT.iterdir()):
        if not subject.is_dir() or subject.name.startswith("."):
            continue
        if selected and subject.name not in selected:
            continue
        check_subject(subject, issues)

    check_docs(issues)
    if not args.no_manifest:
        check_manifest(issues)

    return print_and_report(issues, args.strict, selected, args.json)


if __name__ == "__main__":
    raise SystemExit(main())
