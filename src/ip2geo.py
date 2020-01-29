import json
import requests
from collections import Counter

#cred.json only contains an API_KEY with the format:
#       {API_KEY: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"},
# obtained from ipgeolocation.io


def getCreds(credsFile = "creds.json"):
    API_KEY = ""
    with open(credsFile, "r") as file:
        API_KEY = json.load( file)["API_KEY"]
    return API_KEY

def getIPs(ipsFile = "ipTable.json"):
    IPs = []
    with open(ipsFile, "r") as file:
        IPs = json.load( file)["IPs"]
    return IPs

def getGeo(IPs, credsFile = "creds.json"):
    API_KEY = getCreds(credsFile)
    geos = []
    for IP in IPs:
        response  = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={IP}")
        response = json.loads(response.content)["state_prov"]
        geos.append(response)
    return dict(Counter(geos))
