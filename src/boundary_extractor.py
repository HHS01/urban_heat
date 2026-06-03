import osmnx as ox
import geopandas as gpd
import os
import argparse
from src import config

def fetch_boundary(place_name, output_filename):
    """
    Fetches the boundary of a specific place from OpenStreetMap.
    Generic and reusable for any city or neighborhood.
    """
    print(f"Fetching boundary for: {place_name}")
    try:
        # Fetch the geometry from OSM
        boundary = ox.geocode_to_gdf(place_name)
        
        # Ensure the directory exists
        os.makedirs(config.DATA_RAW, exist_ok=True)
        
        # Save to GeoJSON
        output_path = os.path.join(config.DATA_RAW, f"{output_filename}.geojson")
        boundary.to_file(output_path, driver='GeoJSON')
        
        print(f"Boundary saved to {output_path}")
        return boundary
    except Exception as e:
        print(f"Error fetching boundary for {place_name}: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch boundaries from OpenStreetMap.")
    parser.add_argument("--city", type=str, default=config.CITY_NAME, help="Name of the city (e.g., 'Mumbai, India')")
    parser.add_argument("--settlement", type=str, default=config.SETTLEMENT_NAME, help="Name of the settlement (e.g., 'Dharavi')")
    parser.add_argument("--output_dir", type=str, default=config.DATA_RAW, help="Directory to save the output files")

    args = parser.parse_args()

    # 1. Fetch City Boundary
    city_slug = args.city.split(',')[0].strip().lower().replace(' ', '_')
    fetch_boundary(args.city, f"{city_slug}_boundary")
    
    # 2. Fetch Settlement Boundary
    settlement_slug = args.settlement.lower().replace(' ', '_')
    fetch_boundary(f"{args.settlement}, {args.city}", f"{settlement_slug}_boundary")
