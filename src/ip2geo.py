"""
    transforma las tabla de IPs a un diccionario concentrado de datos
    de los estados

    TODO: consolidar todos los get en una función extra
"""
import os
import json
import requests
from collections import Counter


# cred.json only contains an API_KEY with the format:
#        {API_KEY: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"},
# obtained from ipgeolocation.io


def getCreds(credsFile="creds.json"):
    credsFilePath = os.path.join("..", "creds", credsFile)
    API_KEY = ""
    with open(credsFilePath, "r") as file:
        API_KEY = json.load(file)["API_KEY"]
    return API_KEY


def getIPs(ipsFile="ip_table.json"):
    """
        carga el archivo de IPs
    """
    ipsFilePath = os.path.join("..", "data", ipsFile)
    IPs = []
    with open(ipsFilePath, "r") as file:
        IPs = json.load(file)["IPs"]
    return IPs


def getEquivalencies(eqsFile="equivalencias.json"):
    eqsFilePath = os.path.join("..", "data", eqsFile)
    eqsDict = {}
    with open(eqsFilePath, "r") as file:
        eqsDict = json.load(file)
    return eqsDict


def applyEquivalencies(data):
    eqsDict = getEquivalencies()
    newDict = {}
    for key, value in data.items():
        newDict[eqsDict[key]] = value
    return newDict


def getGeo(IPs, credsFile="creds.json"):
    """
        recibe una lista de IPs y crea un concentrado de datos por estado
    """
    API_KEY = getCreds(credsFile)
    geos = []
    for IP in IPs:
        response = requests.get(
            f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={IP}"
        )
        response = json.loads(response.content)["state_prov"]
        geos.append(response)
    data = dict(Counter(geos))
    return applyEquivalencies(data)


if __name__ == '__main__':
    IPs = getIPs()
    Geo = getGeo(IPs)
    data = applyEquivalencies(Geo)
