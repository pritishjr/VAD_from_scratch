"""Basic scaffold verification tests."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).parents[2]


def test_source_package_exists() -> None:
    assert (PROJECT_ROOT / "src").is_dir()
