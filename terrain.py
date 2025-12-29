from google.colab import drive

drive.flush_and_unmount()
dir = '/content/drive/MyDrive/ColabNotebooks'
drive.mount('/content/drive')

import rasterio
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from rasterio.plot import show
from matplotlib.gridspec import GridSpec
matplotlib.rc('font', size=8)


### create a terrain map for Hong Kong from a .tif file ###
# read the .tif file
elevation = rasterio.open(f'{dir}/Terrain/elevation.tif')
print(elevation)
print("Spatial bounding box =", elevation.bounds, "Dataset width =", elevation.width, "Dataset height =", elevation.height)
left, right, bottom, top = elevation.bounds[0], elevation.bounds[2], elevation.bounds[1], elevation.bounds[3]

# create a terrain matrix from the .tif file
elevation_matrix = elevation.read(1)
missing_data_value = np.nan
max_elev = np.nanmax(elevation_matrix)
min_elev = np.min(elevation_matrix)

# initialise figure
fig = plt.figure(figsize=(15, 6), dpi=300)
ax = plt.subplot(1,1,1)

# create colormap
jet = plt.get_cmap('GnBu', 10)
jetcolors = jet(np.linspace(1, 0, 10))
white = [matplotlib.colors.to_rgba('white')]
mycolors = np.concatenate([white, jetcolors], axis=0)
mycolormap = matplotlib.colors.ListedColormap(mycolors)

# plot as image, set min/max ranges, add the title, axis, and color bar
plt.imshow(elevation_matrix, cmap=mycolormap, vmin=-100, vmax=1000, extent=(left, right, bottom, top))
plt.colorbar().ax.set_title('Meters (m)')
ax = plt.gca()
ax.set_title('Hong Kong Terrain Map')
ax.set_xlabel('Longitude (deg E)')
ax.set_ylabel('Latitude (deg N)')


### create map showing the flood-prone (low-lying) locations in Hong Kong ###
# define the flood-prone altitude (meters) and make the non flood-prone areas as np.nan
altitude = 6
elevation_matrix[((elevation_matrix > altitude) == False) & (elevation_matrix >= 0)] = 1
elevation_matrix[(elevation_matrix > altitude) == True] = np.nan # Sea level rise

# initialise figure
fig = plt.figure(figsize=(15, 6), dpi=300)

# create colormap
jet = plt.get_cmap('RdBu', 2)
jetcolors = jet(np.linspace(0, 1, 2))
white = [matplotlib.colors.to_rgba('white')]
mycolors = np.concatenate([white, jetcolors], axis=0)
mycolormap = matplotlib.colors.ListedColormap(mycolors)

# plot as image, set min/max ranges, add the title and axis
im = plt.imshow(elevation_matrix, cmap=mycolormap, vmin=0, vmax=1, extent=(left, right, bottom, top))
ax = plt.gca()
ax.set_title('Flood-prone Locations in Hong Kong')
ax.set_xlabel('Longitude (deg E)')
ax.set_ylabel('Latitude (deg N)')
