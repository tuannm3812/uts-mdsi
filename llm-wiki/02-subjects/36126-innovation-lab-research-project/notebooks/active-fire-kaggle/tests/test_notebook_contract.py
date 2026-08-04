from pathlib import Path
import sys
import pytest
import nbformat

KAG_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KAG_DIR))

from build_notebook import build_notebook
from build_eda_notebook import build_eda_notebook


EXPECTED_SECTIONS = [
    "1. Project overview",
    "2. Data and methodology",
    "3. Results",
    "4. Reliability analysis",
    "5. Research implications",
    "6. Reproducibility",
]


def test_notebook_has_six_public_sections(tmp_path):
    path = build_notebook(tmp_path / "pilot.ipynb", "tuannm3812/nsw-active-fire-pilot-snapshot")
    notebook = nbformat.read(path, as_version=4)
    headings = [cell.source.split("\n")[0].replace("## ", "").strip() for cell in notebook.cells if cell.cell_type == "markdown" and cell.source.startswith("## ")]
    assert headings == EXPECTED_SECTIONS


def test_notebook_defaults_to_snapshot_cpu_mode(tmp_path):
    path = build_notebook(tmp_path / "pilot.ipynb", "tuannm3812/nsw-active-fire-pilot-snapshot")
    notebook = nbformat.read(path, as_version=4)
    source = "\n".join(cell.source for cell in notebook.cells if cell.cell_type == "code")
    assert 'EXECUTION_MODE = "snapshot"' in source
    assert "enable_gpu" not in source


def test_eda_notebook_contract(tmp_path):
    path = build_eda_notebook(tmp_path / "1_active_fire_eda.ipynb", "tuannm3812/nsw-active-fire-pilot-snapshot")
    notebook = nbformat.read(path, as_version=4)
    source = "\n".join(cell.source for cell in notebook.cells if cell.cell_type == "code")
    assert 'EXECUTION_MODE = "snapshot"' in source
    
    headings = [cell.source.split("\n")[0].replace("## ", "").strip() for cell in notebook.cells if cell.cell_type == "markdown" and cell.source.startswith("## ")]
    assert "1. Spatial Distribution Analysis" in headings
    assert "2. Sensor Attribute Relationships" in headings
