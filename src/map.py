import os
import geopandas as gpd
import numpy as np
from matplotlib import pyplot as plt


def map(ipsData, geoFile="estados_mexico.json"):
    ipsData = {'CX': 3, 'JC': 1}
    geoFilePath = os.path.join("..", "data", geoFile)
    data = gpd.read_file(geoFilePath)
    data["data"] = np.zeros((32, 1))
    for key, value in ipsData.items():
        data.loc[data["id"] == key, "data"] = value

    fig, ax = plt.subplots()
    data.plot(ax=ax,
              column="data",
              cmap="Blues",
              edgecolor='black',
              linewidth=.1
              )
    plt.axis('off')
    fig.savefig(os.path.join("..", "output", "mapa.svg"))
    return data
