from brownie import Lottery, accounts, config, network
from scripts.helper_script import LOCAL_BLOCKCHAIN_ENVIRONMENT
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3
import pytest

def test_get_entrance_fee():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip()
    # Arrange
    lottery = deploy_lottery()
    # Act
    expected_entrance_fee = Web3.toWei(0.0125, "ether")
    entrance_fee = lottery.getEntranceFee()
    # Assert
    assert entrance_fee == expected_entrance_fee
