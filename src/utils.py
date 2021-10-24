import secrets
from eth_account import Account
import json
import os


def random_wallet_generator(save_addres = False):
    # random eth_wallet generator
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    wallet = {"private_key":private_key,"public_addres":acct.address}
    if save_addres:
        with open("random_key_{}.json".format(wallet["public_addres"][0:3]),'w') as f:
            json.dump(wallet,f)

    return wallet


def abi_evaluator(r):
    # gets the json result to an evaluable dict
    r = r["result"]
    r = r[1:]
    r = r[:-1]
    r = r.replace("true","True")
    r = r.replace("false","False")
    r = eval(r)
    return r

class ApiLogins:
    # obtains the different api keys and general information
    def __init__(self):
        this_dir, _= os.path.split(__file__)
        with open(this_dir+"/token.json") as f:
            api_json = json.load(f)
        os.environ["API_ETH"] = api_json["API_KEY_ETH"]
        os.environ["API_POLY"] = api_json["API_KEY_POLY"]
        os.environ["HTTP_POLY_INFURA"] = api_json["INFURA_POLY_HTTP"]
        os.environ["HTTP_ETH_INFURA"] = api_json["INFURA_ETH_HTTP"]
    def __repr__(self) -> str:
        return """API_KEY_ETH: {} \n
        API_KEY_POLY: {} \n
        """.format(API_ETH,API_POLY)

class Wallet:
    # defines a wallet
    def __init__(self,private_key) -> None:
        self.private_key = private_key
        self.wallet = Account.from_key(private_key)
    def public_address(self)-> str:
        return self.wallet.adrress
    def account(self):
        return self.wallet
        
