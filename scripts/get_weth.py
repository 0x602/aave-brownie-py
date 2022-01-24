from scripts.helpful_scripts import *
from brownie import interface

def main():
    get_weth()

def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    account = get_account()
    weth = interface.IWeth(network_config["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    tx.wait(1)
    print("Received 0.1 WETH")
    return tx