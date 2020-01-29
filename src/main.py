from ip2geo import getIPs
from ip2geo import getGeo
from map import map


def main():
    IPs = getIPs()
    GeoData = getGeo(IPs)
    mapa = map(GeoData)
    mapa.plot(column="data")


if __name__ == '__main__':
    main()
