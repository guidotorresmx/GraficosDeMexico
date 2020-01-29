"""
file:///C:/Users/guido/Desktop/teleton/index.html
https://python-visualization.github.io/folium/quickstart.html
https://github.com/python-visualization/branca
https://python-visualization.github.io/folium/quickstart.html
https://www.storybench.org/plot-state-state-data-map-u-s-r/
https://towardsdatascience.com/lets-make-a-map-using-geopandas-pandas-and-matplotlib-to-make-a-chloropleth-map-dddc31c1983d
https://python-graph-gallery.com/292-choropleth-map-with-folium/


"""
import pandas as pd
import folium
from matplotlib import pyplot as plt
from ip2geo import getIPs
from ip2geo import getGeo
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
import squarify    # pip install squarify (algorithm for treemap)


def main():
    IPs = getIPs()
    Geo = getGeo(IPs)
    states = getMap()
    setMap(states, Geo)

if __name__ == '__main__':
    main()



mexico = gpd.read_file("mexicoMap.json")
mexico["data"] = [np.log(random.random()*100) for _ in range(32)]
mexico.plot(column="data",cmap = "YlGn")

mexico.sort_values(by=["data"], inplace = True, ascending = False)
cmap = matplotlib.cm.Blues
mini=min(mexico["data"])
maxi=max(mexico["data"])
norm = matplotlib.colors.Normalize(vmin = mini, vmax = maxi)
colors = [cmap(norm(value)) for value in mexico["data"]]

squarify.plot(sizes=mexico["data"], label=mexico["id"], color = colors)
plt.axis('off')
plt.show()
