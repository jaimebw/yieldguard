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

class ApiLogins:
    
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