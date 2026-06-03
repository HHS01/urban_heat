import os

# Project configuration
CITY_NAME = "Mumbai, India"
SETTLEMENT_NAME = "Dharavi"

# Google Earth Engine Params
# Note: User must authenticate via `ee.Authenticate()` before running scripts
GEE_PROJECT = "your-gee-project-id"  # Replace with your actual GEE project ID

# Data Paths
DATA_RAW = "data/raw"
DATA_CLEAN = "data/clean"
ARTIFACTS = "artifacts"

# Date Ranges for Heat Analysis (Summer months in Mumbai)
SUMMER_START = "2023-03-01"
SUMMER_END = "2023-05-31"

# Thresholds
HEAT_INDEX_THRESHOLD = 35.0  # Celsius
