from ip2geo import getIPs
from ip2geo import getGeo
from map import map
from squares import squares


def main():
    IPs = getIPs()
    GeoData = getGeo(IPs)

    data = map(GeoData, geografia="municipios")
    squares(data)


if __name__ == '__main__':
    main()
