# %%
# import utils.preprocessing as dpp
from utils.settings_and_colors import colors, cw

import xarray as xr
import matplotlib.pyplot as plt

# import utilities.thermo as thermo

import seaborn as sns
import pandas as pd

ds = xr.open_dataset(
    "ipfs://bafybeihfqxfckruepjhrkafaz6xg5a4sepx6ahhv4zds4b3hnfiyj35c5i", engine="zarr"
)

ex = ds.swap_dims({"circle": "circle_time"}).sel(circle_time="2024-09-03")
for circle_time in ex.circle_time.values:
    print(circle_time)
    dt = pd.Timestamp(circle_time).to_pydatetime()
    ex.sel(circle_time=circle_time).omega.plot(y="altitude", label=f"{dt:%m-%d %H:%M}")
plt.legend()
# %%
ex = ds.swap_dims({"circle": "circle_time"}).sel(
    circle_time="2024-09-23-12:00", method="nearest"
)
for circle_time in ex.circle_time.values:
    print(circle_time)
    dt = pd.Timestamp(circle_time).to_pydatetime()
    ex.sel(circle_time=circle_time).omega.plot(y="altitude", label=f"{dt:%m-%d %H:%M}")
plt.legend()

# %%
fig, ax = plt.subplots(1, 1, figsize=(cw / 6, cw / 4))

sns.set_context("paper", font_scale=1.0)
ex = ds.swap_dims({"circle": "circle_time"}).sel(
    circle_time="2024-09-23-10:00", method="nearest"
)
dt = pd.Timestamp(ex.circle_time.values).to_pydatetime()
ex.omega.plot(y="altitude", ax=ax, label=f"{dt:%m-%d %H}hr", lw=2, c=colors["West"])

ex = ds.swap_dims({"circle": "circle_time"}).sel(
    circle_time="2024-09-03-15:00", method="nearest"
)
dt = pd.Timestamp(ex.circle_time.values).to_pydatetime()
ex.omega.plot(y="altitude", ax=ax, label=f"{dt:%m-%d %H}hr", lw=2, c=colors["East"])
sns.despine(offset=10)
ax.set_title(None)
ax.legend(bbox_to_anchor=(-0.5, 0.85), loc="lower left", fontsize=8)

ax.set_yticks([0, 6000, 12000])
ax.set_yticklabels([0, 6, 12])
ax.set_xlabel("$\\omega$ / Pa s$^{-1}$")
ax.set_ylabel("altitude/ km")


# %%
fig, ax = plt.subplots(1, 1, figsize=(cw / 6, cw / 4))

sns.set_context("paper", font_scale=1.0)
ex = ds.swap_dims({"circle": "circle_time"}).sel(
    circle_time="2024-09-03-18:30", method="nearest"
)
dt = pd.Timestamp(ex.circle_time.values).to_pydatetime()
ex.omega.plot(y="altitude", ax=ax, label=f"{dt:%m-%d %H}hr", lw=2, c=colors["North"])

sns.despine(offset=10)
ax.set_title(None)
ax.legend(bbox_to_anchor=(-0.5, 0.85), loc="lower left", fontsize=8)

ax.set_yticks([0, 6000, 12000])
ax.set_yticklabels([0, 6, 12])
ax.set_xlabel("$\\omega$ / Pa s$^{-1}$")
ax.set_ylabel("altitude/ km")


# %%
