import os
import matplotlib
import matplotlib.pyplot as plt
import squarify     # ver instalación


def squares(data):
    data.sort_values(by=["data"], inplace=True, ascending=False)
    cmap = matplotlib.cm.Blues
    mini = min(data["data"])
    maxi = max(data["data"])
    norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
    colors = [cmap(norm(value)) for value in data["data"]]

    fig, ax = plt.subplots()
    squarify.plot(ax=ax, sizes=data.loc[data["data"] != 0]["data"],
                  label=data["name"],
                  color=colors
                  )
    plt.axis('off')
    fig.savefig(os.path.join("..", "output", "cuadros.svg"))
