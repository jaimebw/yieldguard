from src.utils import *
from src.scan import *
from src.act import *
import pandas as pd
wallet = random_wallet_generator()
wallet_data = scan(wallet["public_addres"])
logins = ApiLogins()

def test_util():
    # test random_wallet_generator
    assert len(wallet["private_key"]) == 66
    assert len(wallet["public_addres"]) == 42

def test_scan():
    #wallet = random_wallet_generator()
    assert wallet_data.get_eth_balance() == 0
    assert wallet_data.get_matic_balance() == 0
    assert wallet_data.get_eth_transactions().empty
    assert wallet_data.get_poly_transactions().empty

#def test_terminal_wallet():
#    my_wallet = term_wallet()
    

