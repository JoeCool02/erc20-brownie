from scripts.helpful_scripts import get_account
from brownie import LiftingFaceToken, config, network

INITIAL_SUPPLY = 1000000 * 10 ** 18


def deploy_token():
    account = get_account()
    token = LiftingFaceToken.deploy(
        INITIAL_SUPPLY,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"Deployed Token to {token.address}!")
    return token


def get_token_status():
    account = get_account()
    token = LiftingFaceToken[-1]
    totalSupply = token.totalSupply()
    total_you_own = token.balanceOf(account.address)
    name_of_token = token.name()
    print(f"There are {totalSupply} tokens!")
    print(f"{account.address} owns {total_you_own} {name_of_token} tokens!")
    return token


def main():
    deploy_token()
    get_token_status()
