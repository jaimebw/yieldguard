import requests
import os
import pandas as pd


class scan:
    def __init__(self, eth_addres):

        self.api_key_eth = os.getenv("API_ETH")
        self.api_key_poly = os.getenv("API_POLY")
        self.eth_addres = eth_addres

    def get_eth_balance(self):
        # return ETH balance from wallet
        r = requests.get("https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey={}"\
        .format(self.eth_addres,self.api_key_eth)).json()
        r = int(r["result"])
        return r

    def get_matic_balance(self):
        # return Matic balance from wallet
        r = requests.get("https://api.polygonscan.com/api?module=account&action=balance&address={}&tag=latest&apikey={}"\
        .format(self.eth_addres,self.api_key_poly)).json()
        r = int(r["result"])
        return r

    def get_poly_transactions(self,to_Pandas = False):
        # get transactions from Polygon L2
        r = requests.get("https://api.polygonscan.com/api?module=account&action=txlist&address={}&startblock=1&endblock=99999999&sort=asc&apikey={}"\
        .format(self.eth_addres,self.api_key_poly))
        r = r.json()
        r = r["result"]
        if to_Pandas == False:
            return r
        else:
            r = pd.DataFrame(r)
            return r

    def get_eth_transactions(self,to_Pandas = False):
        # get transactions from ETH L1
        r = requests.get("https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&sort=asc&apikey={}"\
        .format(self.eth_addres,self.api_key_eth))
        r = r.json()
        r = r["result"]
        if to_Pandas == False:
            return r
        else:
            r = pd.DataFrame(r)
            return r
