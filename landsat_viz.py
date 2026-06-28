"""Visualize a local Landsat GeoTIFF with geemap and export an interactive HTML map.

Usage:
    python landsat_viz.py /path/to/landsat.tif [--output landsat_map.html]

Requires the `geemap` package:
    pip install geemap
"""

import argparse
import sys

import geemap


def build_map(landsat_path: str) -> "geemap.Map":
    """Build an interactive map with the given Landsat GeoTIFF added as an RGB raster."""
    m = geemap.Map()
    m.add_raster(
        landsat_path,
        bands=[4, 3, 2],  # Landsat 8/9: B4 (Red), B3 (Green), B2 (Blue)
        layer_name="Landsat",
        vmin=0,
        vmax=3000,
    )
    return m


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("landsat_path", help="Path to the local Landsat GeoTIFF file")
    parser.add_argument(
        "--output",
        default="landsat_map.html",
        help="Output HTML file path (default: landsat_map.html)",
    )
    args = parser.parse_args()

    m = build_map(args.landsat_path)
    m.to_html(filename=args.output, title="Landsat Visualization")
    print(f"Saved interactive map to '{args.output}'.")


if __name__ == "__main__":
    main()
