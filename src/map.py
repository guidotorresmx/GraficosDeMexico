
import os
import geopandas as gpd
import numpy as np
from matplotlib import pyplot as plt


def map(ipsData, geografia):
    """
        TODO: improve merge dicts technique for performance
    """
    geoFile = ""
    if geografia == "estados":
        geoFile = "estados_mexico.json"
    elif geografia == "municipios":
        geoFile = "municipios_mexico.json"
    else:
        raise Exception(f"geografia  = {geografia} no implementada")

    geoFilePath = os.path.join("..", "data", geoFile)
    data = gpd.read_file(geoFilePath)
    data["data"] = np.zeros((len(data), 1))
    for key, value in ipsData.items():
        try:
            data.loc[data["id"] == key, "data"] = value
        finally:
            raise Exception("data no armoniza con mapa")

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
