import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, mapping
import geopandas as gpd
from netCDF4 import Dataset

# Load the grid
ds = xr.open_dataset("../../ciofs-stretching/ciofs.romsgrid_v4.nc")
lon = ds['lon_rho'].values
lat = ds['lat_rho'].values
mask = ds['mask_rho'].values

ny, nx = lon.shape
region_mask = np.zeros_like(mask, dtype=np.int8)

# Helper function
def in_box(latmin, latmax, lonmin, lonmax):
    return (
        (lat >= latmin) & (lat <= latmax) &
        (lon >= lonmin) & (lon <= lonmax) &
        (mask == 1)
    )

# --- Region boundaries ---

# 1: Outside Cook Inlet (Cape Douglas ↔ Port Chatham and south)
lon_west = -153.25
lon_east = -151.9
# Calculate the latitude of the line at each longitude
lat_line = 58.85 + (59.206 - 58.85) * (lon - lon_west) / (lon_east - lon_west)
outside_mask = (lat < lat_line) & (mask == 1)
region_mask[outside_mask] = 5

# 2: Kachemak Bay (East of a line from 59.316907, -151.986815 to 59.751085, -151.861245 and south of ~59.85)

# Define the eastward-sloping line for Kachemak Bay boundary
lat_kbay_west, lon_kbay_west = 59.316907, -151.986815
lat_kbay_east, lon_kbay_east = 59.751085, -151.861245

# Interpolate longitude of the boundary line at each latitude
lon_kbay_line = lon_kbay_west + (lon_kbay_east - lon_kbay_west) * (lat - lat_kbay_west) / (lat_kbay_east - lat_kbay_west)

# Set a common upper latitude boundary for both Kachemak Bay and Central Cook Inlet
lat_east_boundary = 59.83  # or another value you prefer for both

# Define the upper latitude boundary for Kachemak Bay as a line between (lat_kbay_east, lon_kbay_east) and (59.867291, -150.908574)
lat_kbay_upper_east, lon_kbay_upper_east = 59.867291, -150.908574

# Interpolate the latitude of the upper boundary at each longitude
lat_kbay_upper_line = lat_kbay_east + (lat_kbay_upper_east - lat_kbay_east) * (lon - lon_kbay_east) / (lon_kbay_upper_east - lon_kbay_east)

kbay_mask = (
    (lat >= 59.38) & (lat <= lat_kbay_upper_line) &
    (lon >= lon_kbay_line) &  # east of the line
    (mask == 1)
)
region_mask[kbay_mask] = 4

# 3: Lower Cook Inlet (between Outside and Anchor Point ↔ Chinitna Bay)

# Define upper boundary line for Lower Cook Inlet
lon_lower_west = -152.73
lon_lower_east = -151.865
lat_line_upper = 59.905 + (59.764 - 59.905) * (lon - lon_lower_west) / (lon_lower_east - lon_lower_west)

lower_mask = (
    (lat >= lat_line) & (lat <= lat_line_upper) &
    (lon < lon_kbay_line) &  # west of the Kachemak Bay line
    (region_mask == 0) &
    (mask == 1)
)
region_mask[lower_mask] = 3

# 4: Central Cook Inlet (between Anchor Point ↔ Chinitna Bay and the Forelands)

# Define the latitude boundary line for Upper Cook Inlet between (-151.716, 60.712) and (-151.41, 60.71)
lon_upper_west, lat_upper_west = -151.716, 60.712
lon_upper_east, lat_upper_east = -151.41, 60.71

lat_upper_line = lat_upper_west + (lat_upper_east - lat_upper_west) * (lon - lon_upper_west) / (lon_upper_east - lon_upper_west)

# line for between Central and Upper CI
lat_upper_east2, lon_upper_east2 = 60.711754, -151.708143
lat_upper_west2, lon_upper_west2 = 60.831986, -151.886307

lat_upper_line2 = lat_upper_west2 + (lat_upper_east2 - lat_upper_west2) * (lon - lon_upper_west2) / (lon_upper_east2 - lon_upper_west2)

# central_mask = (
#     (lat > lat_line_upper) & (lat <= 60.75) &
#     (region_mask == 0) &
#     (mask == 1)
# )
central_mask = (
    (lat > lat_line_upper) &
    (
        ((lon <= lon_upper_west) & (lat <= lat_upper_line2)) |  # west: use lat_upper_line2
        ((lon > lon_upper_west) & (lat <= lat_upper_line))     # east: use lat_upper_line (or adjust as needed)
    ) &
    (region_mask == 0) &
    (mask == 1)
)
region_mask[central_mask] = 2

# 5: Upper Cook Inlet (north of Forelands ~60.75°N)

# 5: Upper Cook Inlet (north of the boundary line)
# upper_mask = (lat > lat_upper_line) & (mask == 1)
upper_mask = (
    (
        ((lon <= lon_upper_west) & (lat > lat_upper_line2)) |  # west: use lat_upper_line2
        ((lon > lon_upper_west) & (lat > lat_upper_line))     # east: use lat_upper_line (or adjust as needed)
    ) &
    (mask == 1)
)
region_mask[upper_mask] = 1

# --- Create polygons from masks ---
region_names = {
    5: "Outside Cook Inlet",
    4: "Kachemak Bay",
    3: "Lower Cook Inlet",
    2: "Central Cook Inlet",
    1: "Upper Cook Inlet"
}

polygons = []
region_ids = []
names = []

for rid in range(1, 6):
    points = np.column_stack((lon[region_mask == rid], lat[region_mask == rid]))
    if len(points) == 0:
        continue
    poly = Polygon(points).convex_hull
    polygons.append(poly)
    region_ids.append(rid)
    names.append(region_names[rid])

gdf = gpd.GeoDataFrame({'region_id': region_ids, 'name': names}, geometry=polygons, crs="EPSG:4326")
gdf.to_file("cook_inlet_regions.geojson", driver="GeoJSON")

# --- Save NetCDF region mask ---
with Dataset("cook_inlet_region_mask.nc", "w", format="NETCDF4") as nc:
    nc.createDimension("eta_rho", ny)
    nc.createDimension("xi_rho", nx)
    var = nc.createVariable("region_id", "i1", ("eta_rho", "xi_rho"))
    var[:] = region_mask
    var.long_name = "Cook Inlet region ID mask"
    var.flag_values = np.array(list(region_names.keys()), dtype="i1")
    var.flag_meanings = " ".join(name.replace(" ", "_") for name in region_names.values())

# --- Plot
# fig, ax = plt.subplots(figsize=(10, 8))
# p = ax.pcolormesh(lon, lat, region_mask, cmap="tab10", shading="auto")
# for poly, name in zip(polygons, names):
#     ax.plot(*poly.exterior.xy, color='k')
#     ax.annotate(name, xy=poly.centroid.coords[0], ha='center', fontsize=10, color='white')
# ax.set_title("Cook Inlet Subregions (from CIOFS grid)")
# plt.colorbar(p, ax=ax, label="Region ID")
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.tight_layout()
# plt.savefig("cook_inlet_regions_new.png", dpi=150)
# plt.show()
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import ListedColormap, BoundaryNorm

# --- Plot with Cartopy ---
fig = plt.figure(figsize=(10, 8))

# Alaska-friendly projection
proj = ccrs.AlbersEqualArea(central_longitude=-154.0, central_latitude=50.0,
                             standard_parallels=(55.0, 65.0))
ax = plt.axes(projection=proj)

# Build list of IDs including 0 (background)
used_ids = sorted(np.unique(region_mask))
used_names = ["Outside domain" if i == 0 else region_names[i] for i in used_ids]

# Define colors: background color first, then regions
base_colors = ["lightblue"] + list(plt.cm.tab10.colors[:len(used_ids)-1])
cmap = ListedColormap(base_colors)
norm = BoundaryNorm([i - 0.5 for i in range(len(used_ids) + 1)], cmap.N)

# Plot mask
p = ax.pcolormesh(lon, lat, region_mask, cmap=cmap, norm=norm, shading="auto",
                  transform=ccrs.PlateCarree())

# Add polygons + labels
for poly, name in zip(polygons, names):
    ax.plot(*poly.exterior.xy, color="k", transform=ccrs.PlateCarree())
    ax.annotate(name, xy=poly.centroid.coords[0], transform=ccrs.PlateCarree(),
                ha="center", fontsize=9, color="white")

# Land and coastlines
ax.add_feature(cfeature.LAND, facecolor="lightgray", zorder=1)
ax.coastlines(resolution="10m", linewidth=0.8)

# Colorbar with custom tick labels
cbar = plt.colorbar(p, ax=ax, shrink=0.7, pad=0.05, ticks=used_ids)
cbar.ax.set_yticklabels(used_names)
cbar.set_label("Cook Inlet Regions")

# Add lat/lon gridlines with labels
gl = ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
gl.top_labels = False
gl.right_labels = False
gl.xlabel_style = {"size": 10}
gl.ylabel_style = {"size": 10}

ax.set_title("Cook Inlet Subregions (CIOFS grid)")
plt.tight_layout()
plt.savefig("figures/cook_inlet_regions.png", dpi=150, bbox_inches="tight")
plt.show()
