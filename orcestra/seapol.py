# %%
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import pandas as pd
import seaborn as sns

from matplotlib.colors import ListedColormap
from utils.settings_and_colors import load_colormap_from_txt, cw, colors

# %%

colormap_file = "chase-spectral-rgb.txt"  # Replace with your .txt file path
radar_cmap = load_colormap_from_txt(colormap_file)
discrete_cmap = ListedColormap(radar_cmap(np.linspace(0, 1, 16)))
discrete_mask_cmap = discrete_cmap.copy()
discrete_mask_cmap.set_under(color="white")  # set values below vmin to white
discrete_mask_cmap.set_bad(color="gray")  # set missing (NaN) values to gray

discrete_mask_cmap
# %%
time_map1 = np.datetime64("2024-09-23T12:00")
str_map1 = "2024-09-23 12:00"
time_map2 = np.datetime64("2024-09-03T15:00")  # really the merged circle from 1500-1520
str_map2 = "2024-09-03 15:00 - 15:20"

seapol = xr.open_dataset(
    "ipfs://bafybeigdehy7635uypwipv5xdnlvgnlbncvuyudajwejawn2llirbp2vyq", engine="zarr"
)
# Find indices
index_map1 = np.abs(pd.to_datetime(seapol.time) - time_map1).argmin()
map1 = seapol.DBZ[index_map1, :, :]
map2 = xr.open_dataset(
    "/Users/m219063/work/data/orcestra/gridded_composite_20240903_1500.nc",
    engine="netcdf4",
).DBZ[0, :, :]
# %%
# Make plot

sns.set_context("paper", font_scale=1.0)
fig, axs = plt.subplots(1, 2, figsize=(cw / 1.5, cw / 3.5))  # 1 row, 2 column

# Limit to within 120 km of center
ix = np.where((map1.X >= -120000) & (map1.X <= 120000))[0]
iy = np.where((map1.Y >= -120000) & (map1.Y <= 120000))[0]

seapol_west = axs[0].pcolormesh(
    map1.longitude[ix, iy],
    map1.latitude[ix, iy],
    map1[ix, iy],
    cmap=discrete_mask_cmap,
    vmin=-10,
    vmax=60,
    shading="auto",
)
axs[0].set_aspect("equal", adjustable="box")

axs[0].set_ylabel("Latitude / deg N")
axs[0].set_xlabel("Longitude / deg E")
axs[0].set_xticks([-60, -59])
axs[0].set_yticks([13, 14])
axs[0].set_xticklabels(axs[0].get_xticklabels())
axs[0].set_yticklabels(
    axs[0].get_yticklabels(),
)
axs[0].spines["left"].set_color(colors["West"])
axs[0].spines["bottom"].set_color(colors["West"])
axs[0].tick_params(color=colors["West"])

seapol_east = axs[1].pcolormesh(
    map2.longitude[ix, iy],
    map2.latitude[ix, iy],
    map2[ix, iy],
    cmap=discrete_mask_cmap,
    vmin=-10,
    vmax=60,
    shading="auto",
)
axs[1].set_aspect("equal", adjustable="box")

# axs[1].set_ylabel('Latitude / deg N')
axs[1].set_xlabel("Longitude / deg E")
axs[1].set_xticks([-31, -30])
axs[1].set_yticks([8, 9])
axs[1].set_xticklabels(axs[1].get_xticklabels())
axs[1].set_yticklabels(axs[1].get_yticklabels())

# Add 60 km circle
axs[0].add_patch(
    plt.Circle(
        (map1.longitude[245, 245], map1.latitude[245, 245]),
        60 / 111.32,
        color="gray",
        alpha=0.7,
        fill=False,
        linestyle="--",
        linewidth=0.5,
    )
)
axs[1].add_patch(
    plt.Circle(
        (map2.longitude[245, 245], map2.latitude[245, 245]),
        60 / 111.32,
        color="gray",
        alpha=0.7,
        fill=False,
        linestyle="--",
        linewidth=0.5,
    )
)
sns.despine(offset=10)
axs[1].spines["left"].set_color(colors["East"])
axs[1].spines["bottom"].set_color(colors["East"])
axs[1].tick_params(color=colors["East"])

# cax = inset_axes(axs[0], width="3%", height="40%", loc='upper right')

cax = fig.add_axes([0.32, 0.75, 0.18, 0.03])
cbar = fig.colorbar(seapol_east, cax=cax, orientation="horizontal", location="top")
cbar.outline.set_visible(False)
cbar.set_label("Radar reflectivity / dBZ")

plt.savefig("seapol_case_overview_zoom.png", dpi=300)

# %%
