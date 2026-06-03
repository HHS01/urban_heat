# Project Strategy: Hyperlocal Urban Heat Risk Map

A hyperlocal urban heat risk map for informal settlements using free satellite data — with a simple dashboard or alert system.

---

## Phase 1 — City Selection
Selecting the right city is crucial to avoid data acquisition bottlenecks.

**Criteria:**
- Presence of large informal settlements.
- Hot climate with significant heat stress.
- Reliable satellite coverage.

**Target Candidates:**
- Dhaka, Bangladesh
- Nairobi, Kenya (Kibera)
- Lagos, Nigeria
- Mumbai, India (Dharavi)
- Accra, Ghana

*Action: Pick one city and one specific settlement to maintain focus.*

---

## Phase 2 — Data Collection
Utilizing free and open-source data repositories.

### Heat Data
- **NASA MODIS:** Land surface temperature (LST), global, free (via Google Earth Engine or NASA Earthdata).
- **Landsat 8/9:** Higher resolution thermal bands, free (via Google Earth Engine).

### Settlement Boundaries
- **GHSL (Global Human Settlement Layer):** EU dataset for built-up density.
- **OpenStreetMap:** Community-mapped informal settlement outlines.
- **HDX (Humanitarian Data Exchange):** Country-specific shapefiles.

### Weather & Environment
- **Open-Meteo API:** Free historical and forecast weather data.
- **OpenWeatherMap:** Free tier for current weather.
- **WorldPop:** Population density mapping.
- **DHS Program:** Health and wealth survey data for socioeconomic proxies.

---

## Phase 3 — Analysis Pipeline
Developing a robust data processing flow.

**Tech Stack:**
- **Language:** Python
- **Processing:** Google Earth Engine Python API
- **Spatial Data:** GeoPandas, Rasterio
- **Indices:** NDVI (Vegetation), NDBI (Built-up)
- **Modeling:** Scikit-learn for risk scoring

**Workflow:**
1. Extract Land Surface Temperature (LST) from satellite imagery.
2. Overlay with settlement boundaries.
3. Calculate heat anomaly vs. city average.
4. Layer vulnerability indicators (density, lack of greenness).
5. Produce risk score per zone.

---

## Phase 4 — Visible Outputs
Creating tangible deliverables for the project portfolio.

- **Option A: Interactive Map (Recommended):** Use `Folium` or `Kepler.gl` for heat overlays and hotspots.
- **Option B: Simple Dashboard:** Build a `Streamlit` app to show trends and risk comparisons.
- **Option C: Alert Prototype:** Integrate `Open-Meteo` to trigger simulated heat alerts based on LST thresholds.

---

## Phase 5 — Impact Analysis (The "So What" Layer)
Turning data into policy-relevant insights.

- Identify the hottest and most densely populated zones.
- Analyze temporal trends (5-10 years) using historical MODIS data.
- Prioritize high-impact intervention sites (e.g., tree planting, cool roofs).
- Estimate population exposure to dangerous heat days.

---

## Project Timeline

| Week | Task |
|---|---|
| 1 | City selection and initial LST data exploration in GEE |
| 2 | Data cleaning and settlement boundary overlays |
| 3 | Computation of heat anomalies and vulnerability index |
| 4 | Development of the interactive map or dashboard |
| 5 | Temporal analysis and trend identification |
| 6 | Documentation, final write-up, and GitHub deployment |

---

## Immediate First Step
Sign up for a free **Google Earth Engine** account: [https://earthengine.google.com/signup](https://earthengine.google.com/signup)
Run an LST tutorial to generate your first temperature map.
