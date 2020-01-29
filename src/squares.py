import pandas as pd
import requests
import json
from IPython.display import HTML, display
import random
import geopandas as gpd
import random
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import squarify  #ver instalación


mexico.sort_values(by=["data"], inplace = True, ascending = False)
cmap = matplotlib.cm.Blues
mini=min(mexico["data"])
maxi=max(mexico["data"])
norm = matplotlib.colors.Normalize(vmin = mini, vmax = maxi)
colors = [cmap(norm(value)) for value in mexico["data"]]

squarify.plot(sizes=mexico["data"], label=mexico["id"], color = colors)
plt.axis('off')
plt.show()
