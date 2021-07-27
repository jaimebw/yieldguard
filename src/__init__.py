import os
import json
import warning

with open("src/token.json") as f:
    api_json = json.load(f)

try:
    os.environ["API_ETH"] = api_json["API_KEY_ETH"]
    os.environ["API_POLY"] = api_json["API_KEY_POLY"]
except:
    raise AttributeError("Faltan las API_KEYs")
try:
    os.environ["HTTP_POLY_INFURA"] = api_json["INFURA_POLY_HTTP"]
    os.environ["HTTP_ETH_INFURA"] = api_json["INFURA_ETH_HTTP"]
except:
    warning.warn("You didnt gave access the Infura node!\n You may connect to a random node or personal node")
