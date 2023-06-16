import os, json
from web3 import Web3, HTTPProvider

# abi
current_path = os.path.dirname(__file__)
with open(current_path + "/abi/erc721.json") as f:
    erc721ABI = json.load(f)

ZksRPC = 'https://mainnet.era.zksync.io'
web3 = Web3(HTTPProvider(ZksRPC))

def getNFTBalance(contractAddress, walletAddress):
    contract = web3.eth.contract(address=Web3.to_checksum_address(contractAddress), abi=erc721ABI)
    balance = contract.functions.balanceOf(Web3.to_checksum_address(walletAddress)).call()
    print(f'balance={balance}')
    return balance 

if __name__ == '__main__':
    getNFTBalance('', '')