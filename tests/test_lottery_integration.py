from brownie import network
from scripts.deploy_lottery import deploy_lottery
from scripts.helper_script import LOCAL_BLOCKCHAIN_ENVIRONMENT, fund_with_link, get_account
import pytest
import time


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    fund_with_link(lottery)
    lottery.endLottery({"from": account})
    time.sleep(240)
    print(account)
    print(lottery.recentWinner())
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0