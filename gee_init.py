"""Initialize and validate a Google Earth Engine (GEE) session.

Usage:
    python gee_init.py

Requires the `earthengine-api` package:
    pip install earthengine-api
"""

import sys

PROJECT_ID = "jyang-testing"


def authenticate_and_initialize(project_id: str = PROJECT_ID):
    """Authenticate (if needed) and initialize Earth Engine for the given project."""
    import ee

    try:
        ee.Initialize(project=project_id)
    except Exception:
        ee.Authenticate()
        ee.Initialize(project=project_id)

    return ee


def validate_project(ee, project_id: str = PROJECT_ID) -> bool:
    """Run a lightweight request to confirm credentials and project access are valid."""
    try:
        info = ee.Number(1).add(1).getInfo()
        if info != 2:
            raise RuntimeError("Unexpected response from Earth Engine backend.")
        print(f"GEE initialized and validated successfully for project '{project_id}'.")
        return True
    except Exception as exc:
        print(f"GEE validation failed for project '{project_id}': {exc}", file=sys.stderr)
        return False


def main():
    ee = authenticate_and_initialize(PROJECT_ID)
    ok = validate_project(ee, PROJECT_ID)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
