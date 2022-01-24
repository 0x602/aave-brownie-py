from brownie.network import account
from scripts.aave_borrow import approve_erc20, get_asset_price, get_lending_pool
from scripts.helpful_scripts import *


def test_get_asset_price():
    # Arrange / Act
    asset_price = get_asset_price(network_config["dai_eth_price_feed"])
    # Assert
    assert asset_price > 0


def test_get_lending_pool():
    # Arrange / Act
    lending_pool = get_lending_pool()
    # Assert
    assert lending_pool is not None


def test_approve_erc20():
    # Arrange
    account = get_account()
    lending_pool = get_lending_pool()
    amount = 10 ** 18 # 1
    erc20_address = network_config["weth_token"]
    # Act
    tx = approve_erc20(amount, lending_pool.address, erc20_address, account)
    # Assert
    assert tx is not True