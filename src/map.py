import os
import geopandas as gpd
import numpy as np


def map(data, geoFile="estados_mexico.json"):
    data = {'CX': 3, 'JC': 1}
    geoFilePath = os.path.join("..", "data", geoFile)
    mexico = gpd.read_file(geoFilePath)
    mexico["data"] = np.zeros((32, 1))
    for key, value in data.items():
        print(key)
        print(value)
        mexico.loc[mexico["id"] == key, "data"] = value
    return mexico
