#!/usr/bin/env python3

import rasterio
from rasterio.enums import Resampling
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

import sys
sys.path.append('../../hennes-data/data')
from fav_cmap import wbgyr

factor = 1

with rasterio.open("../../ETOPO_2022_v1_60s_N90W180_surface.tif") as src:
    new_height = src.height // factor
    new_width  = src.width  // factor

    topo_coarse = src.read( 1, out_shape=(new_height, new_width), resampling=Resampling.average )

    bounds = src.bounds
    lons = np.linspace(bounds.left, bounds.right, new_width)
    lats = np.linspace(bounds.top, bounds.bottom, new_height)

ny, nx = topo_coarse.shape
lons_topo = np.linspace(bounds.left, bounds.right, nx)
lats_topo = np.linspace(bounds.top, bounds.bottom, ny)
Lon_topo, Lat_topo = np.meshgrid(lons_topo, lats_topo)

# Earth radius
R_earth = 6.371e6  # m

# Angular spacings (radians)
dlon = np.deg2rad(lons_topo[1] - lons_topo[0])
dlat = np.deg2rad(lats_topo[0] - lats_topo[1])  # lat decreases

# Raw angular gradients
dh_dphi, dh_dlam = np.gradient(topo_coarse, dlat, dlon)

# Metric factors
lat_rad = np.deg2rad(Lat_topo)

dh_dx = dh_dlam / (R_earth * np.cos(lat_rad))
dh_dy = dh_dphi / R_earth

S = np.sqrt(dh_dx**2 + dh_dy**2)

# Mask poles
S[np.abs(Lat_topo) > 89.5] = np.nan

land_mask = topo_coarse > 0
water_mask = topo_coarse < 0

S_land = np.where(land_mask, S, np.nan)
S_water = np.where(water_mask, S, np.nan)

# Color scale for land is based on land gradients only, not the (much
# larger) gradients found at ocean trenches/ridges.
land_vmin, land_vmax = np.nanmin(S_land), 0.25 * np.nanmax(S_land)
water_vmin, water_vmax = np.nanmin(S_water), 0.25 * np.nanmax(S_water)

land_cmap = wbgyr()
land_cmap.set_bad('none')

# Restrict to the upper half of Blues so flat ocean is already a deep
# blue, and rougher bathymetry (larger S) shades darker still.
ocean_cmap = LinearSegmentedColormap.from_list(
    'ocean', plt.cm.Blues(np.linspace(0.45, 1.0, 256))
)
ocean_cmap.set_bad('none')

# 300 dpi at 20x10 in gives a 6000x3000 px raster embedded in the PDF —
# well above native ETOPO 60" resolution (~21600x10800 for the full
# globe) is overkill and balloons file size, but 300 dpi still far
# exceeds any screen zoom level a talk-locations map will see.
dpi=300
fig = plt.figure(figsize=(20, 10), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow( S_water, extent=[bounds.left, bounds.right, bounds.bottom, bounds.top], cmap=ocean_cmap, vmin=water_vmin, vmax=water_vmax )
ax.imshow( S_land, extent=[bounds.left, bounds.right, bounds.bottom, bounds.top], cmap='Greens', vmin=land_vmin, vmax=land_vmax )
ax.set_axis_off()
plt.savefig("../images/map.pdf", dpi=dpi, bbox_inches=None, pad_inches=0)

# Web copy: the talk map (Leaflet imageOverlay) caps its max zoom at this
# image's native pixel width (see _scripts/talkmap_assets/map.html), where
# nativeZoom = log2(width / 256). Each doubling of width buys one more zoom
# level, so going from 200 to 800 dpi (4000x2000 -> 16000x8000 px, a 4x
# width increase) buys log2(4) = 2 full zoom levels versus the previous
# version, without upsampling: native ETOPO 60" resolution is 21600x10800,
# comfortably above 16000x8000. JPEG instead of PNG keeps the file size
# sane since this is a continuous-tone image with no sharp edges or
# transparency to lose.
fig.savefig("../images/map.jpg", dpi=800, bbox_inches=None, pad_inches=0,
            pil_kwargs={"quality": 88, "optimize": True})

plt.show()
plt.close()
