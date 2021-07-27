import secrets
import web3
from eth_account import Account
import json


def random_wallet_generator(save_addres = False):
    # random eth_wallet generator
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    wallet = {"private_key":private_key,"public_addres":acct.address}
    if save_addres is True:
        with open("random_key_{}.json".format(wallet["public_addres"][0:3]),'w') as f:
            json.dump(wallet,f)

    return wallet

