# Simple Terrain Visualisationand Flood Risk Analysis

This repository contains Python code developed in Google Colab for geospatial analysis of Hong Kong's terrain elevation data and identification of flood-prone areas. The analysis visualizes elevation patterns and highlights low-lying regions vulnerable to flooding at a 6-meter threshold, using public raster datasets.
​
### Objectives
The primary goal is to demonstrate terrain mapping and flood risk assessment using open-source Python libraries and Hong Kong's official Digital Terrain Model (DTM) data. Key objectives include loading GeoTIFF elevation files, creating custom colormaps for visualization, and thresholding data to isolate areas below 6 meters—relevant given that about 15% of Hong Kong's land is below 5 meters above principal datum.
​
This supports climate risk analytics, urban planning, and sea-level rise studies, aligning with high-resolution DEMs (e.g., 50cm resolution from Lands Department) available via the Hong Kong Geodata Store.
​
### Usage Steps
1. Run Terrain Visualization: Loads .tif, extracts elevation matrix, applies custom GnBu colormap (white for missing/sea, green-to-blue for 0-1000m), and plots with bounds, labels, and colorbar.​
2. Generate Flood Map: Select areas ≤6m (and ≥0m), uses RdBu colormap for binary flood-prone visualization (white=not impacted, blue=with risk of flooding).
3. Outputs: Figures displaying longitude/latitude extent; adjust ```altitude=6``` for different scenarios.

### Key Code Features
Raster Reading: ```rasterio.open()``` for metadata (bounds, width/height) and ```read(1)``` for elevation band.​
Colormap Customization: Concatenates white with ```ListedColormap``` for intuitive sea/terrain rendering.
Flood Thresholding: ```np.where()``` logic isolates low elevations; NaN handling for non-flood areas and sea/water-bodies.
Plotting: ```plt.imshow()``` with extent for georeferenced display; GridSpec ready for multi-panel extensions.

### Results
![](/Results/terrain.png)
![](/Results/flood-prone-area.png)

### Limitations and Extensions
- Assumes single-band elevation GeoTIFF.
- Binary thresholding ignores runoff, drainage; integrate with geopandas for vector overlays.
- For production: Use local paths instead of Drive; add CRS reprojection if needed (```elevation.crs```).
- Future: Adjust sea-level rise scenarios (e.g., +1m) or slope analysis.

### Attribution
Attribute data sources: Lands Department (Hong Kong) DTMs.
