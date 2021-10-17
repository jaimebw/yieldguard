import requests
import os
from .utils import ApiLogins
import pandas as pd

class scan(ApiLogins):
    def __init__(self, eth_addres):
        super().__init__()
        self.api_key_eth = os.getenv("API_ETH")
        self.api_key_poly = os.getenv("API_POLY")
        self.eth_addres = eth_addres


    def get_eth_balance(self)->float:
        # return ETH balance from wallet
        payload = {"address":self.eth_addres,"apikey": self.api_key_eth}
        r = requests.get("https://api.etherscan.io/api?module=account&action=balance",
        params=payload)
        if r.status_code == requests.codes.ok:
            r = r.json()
            ether_count = int(r["result"])/1e18
            return ether_count
        else:
            raise KeyError("Bad Api response")
        

    def get_matic_balance(self)->float:
        # return Matic balance from wallet
        payload = {"address":self.eth_addres,"apikey": self.api_key_poly}
        r = requests.get("https://api.polygonscan.com/api?module=account&action=balance",
        params= payload)
        if r.status_code == requests.codes.ok:
            r = r.json()
            matic_count = int(r["result"])/1e18
            return round(matic_count,2)
        else:
            raise KeyError("Bad Api response")
       
        
    def get_eth_transactions(self):
        # get transactions from ETH L1
        payload = {"address":self.eth_addres,"apikey": self.api_key_eth}
        r = requests.get("https://api.etherscan.io/api?module=account&action=txlist",
        params= payload)
        if r.status_code == requests.codes.ok:
            r = r.json()["result"]
            df = pd.DataFrame(r)
            return df
        else:
            raise KeyError("Bad Api response")


    def get_poly_transactions(self):
        # get transactions from Polygon L2
        payload = {"address":self.eth_addres,"apikey": self.api_key_poly}
        r = requests.get("https://api.polygonscan.com/api?module=account&action=txlist",
        params= payload)
        if r.status_code == requests.codes.ok:
            r = r.json()["result"]
            df = pd.DataFrame(r)
            return df
        else:
            raise KeyError("Bad Api response")



    