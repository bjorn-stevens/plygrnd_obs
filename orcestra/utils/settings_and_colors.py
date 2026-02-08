import numpy as np

cw = 190 / 25.4

colors = {
    "rapsodi": "navy",
    "beach": "teal",
    "gate": "orangered",
    "orcestra": "royalblue",
    "jra3q": "#435D00",
    "merra2": "#6C9600",
    "era5": "#98D500",
    "best": "#00A9A0",
    "pirata12": "#939494",
    "pirata4": "#D9F407",
    "North": "#FF7982",
    "East": "#B6001E",
    "West": "#00b4d8",
}


gate_A = np.array(
    [
        [-27.0, 6.5],
        [-23.5, 5.0],
        [-20.0, 6.5],
        [-20.0, 10.5],
        [-23.5, 12.0],
        [-27.0, 10.5],
    ]
)

gate_B = np.array(
    [
        [-23.5, 7.0],
        [-24.8, 7.8],
        [-24.8, 9.2],
        [-23.5, 10.0],
        [-22.2, 9.2],
        [-22.2, 7.8],
        [-23.5, 7.0],
    ]
)

itcz = np.array([[-34.0, 6], [-20, 6], [-20, 11], [-34.0, 11]])

percusion_E = np.array([[-34.0, 12.5], [-20.0, 12.5], [-20.0, 4.5], [-34.0, 4.5]])


def load_colormap_from_txt(file_path):
    from matplotlib.colors import ListedColormap

    rgb_values = np.loadtxt(file_path)
    return ListedColormap(rgb_values)


# Example usage
colormap_file = "chase-spectral-rgb.txt"  # Replace with your .txt file path
radar_cmap = load_colormap_from_txt(colormap_file)
