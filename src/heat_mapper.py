import ee
import argparse
import json
from src import config

def initialize_gee(project_id=None):
    """Initializes Google Earth Engine."""
    try:
        project = project_id if project_id else config.GEE_PROJECT
        ee.Initialize(project=project)
        print(f"GEE initialized with project: {project}")
    except Exception as e:
        print(f"Error: GEE not initialized. {e}")
        print("Please run `ee.Authenticate()` first if you haven't.")

def get_land_surface_temperature(roi, start_date, end_date):
    """
    Calculates Land Surface Temperature (LST) from Landsat 8 for a ROI.
    Generic function that can be used with any region of interest (roi).
    """
    # Load Landsat 8 Collection 2 Level 2 (Surface Temperature)
    landsat = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2") \
        .filterBounds(roi) \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.lt('CLOUD_COVER', 10))
    
    if landsat.size().getInfo() == 0:
        print(f"No low-cloud images found for the period {start_date} to {end_date}")
        return None

    def calc_lst(image):
        # ST_B10 is Surface Temperature band in Kelvin for Landsat 8
        # Scale factor and offset for Collection 2 Level 2
        thermal = image.select('ST_B10').multiply(0.00341802).add(149.0)
        lst_celsius = thermal.subtract(273.15).rename('LST_Celsius')
        return image.addBands(lst_celsius)

    processed_collection = landsat.map(calc_lst)
    
    # Get the median LST over the period
    median_lst = processed_collection.select('LST_Celsius').median().clip(roi)
    
    return median_lst

def get_ndvi(roi, start_date, end_date):
    """Calculates NDVI (Vegetation Index) - higher is greener."""
    landsat = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2") \
        .filterBounds(roi) \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.lt('CLOUD_COVER', 10))
    
    if landsat.size().getInfo() == 0:
        return None

    def calc_ndvi(image):
        # Landsat 8: B5 is NIR, B4 is Red
        ndvi = image.normalizedDifference(['SR_B5', 'SR_B4']).rename('NDVI')
        return image.addBands(ndvi)
    
    median_ndvi = landsat.map(calc_ndvi).select('NDVI').median().clip(roi)
    return median_ndvi

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process LST and NDVI data using Google Earth Engine.")
    parser.add_argument("--project", type=str, default=config.GEE_PROJECT, help="GEE Project ID")
    parser.add_argument("--start_date", type=str, default=config.SUMMER_START, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end_date", type=str, default=config.SUMMER_END, help="End date (YYYY-MM-DD)")
    parser.add_argument("--geojson", type=str, help="Path to a GeoJSON file for the ROI")
    parser.add_argument("--lat", type=float, help="Latitude of center point (if no geojson)")
    parser.add_argument("--lon", type=float, help="Longitude of center point (if no geojson)")
    parser.add_argument("--buffer", type=int, default=5000, help="Buffer distance in meters for point ROI")

    args = parser.parse_args()

    initialize_gee(args.project)

    # Define ROI
    roi = None
    if args.geojson:
        with open(args.geojson) as f:
            data = json.load(f)
            # Simplistic conversion: use the first feature's geometry
            features = data['features']
            if features:
                geometry = features[0]['geometry']
                roi = ee.Geometry(geometry)
                print(f"ROI loaded from {args.geojson}")
    elif args.lat and args.lon:
        roi = ee.Geometry.Point([args.lon, args.lat]).buffer(args.buffer)
        print(f"ROI created from point: {args.lat}, {args.lon} with {args.buffer}m buffer")
    else:
        # Default to Mumbai center if nothing provided
        roi = ee.Geometry.Point([72.87, 19.07]).buffer(args.buffer)
        print(f"No ROI provided. Defaulting to Mumbai center with {args.buffer}m buffer.")

    if roi:
        lst_map = get_land_surface_temperature(roi, args.start_date, args.end_date)
        ndvi_map = get_ndvi(roi, args.start_date, args.end_date)
        
        if lst_map:
            print("LST and NDVI maps processed successfully.")
            # Note: In a real scenario, you'd export these to GEE Assets or Drive
            print("Ready for export to GEE Assets or Drive.")
