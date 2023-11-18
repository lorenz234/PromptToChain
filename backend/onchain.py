import pandas as pd
from web3 import Web3

class onchain_stuff:
    def __init__(self, provider, contract_address, contract_abi, owner_address, owner_pk):
        self.w3 = Web3(Web3.HTTPProvider(provider))
        self.owner_address = owner_address
        self.pk = owner_pk
        self.contract_address = contract_address
        self.abi = contract_abi
        self.contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)
        self.contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)
    def checkNFTmint(self):
        return self.contract.functions.tokenIdCounter().call()
    def getprompt(self):
        return pd.read_csv('prompt.txt')
    def send_new_url_transaction(self, tokenId, new_url):
        nonce = self.w3.eth.get_transaction_count(self.owner_address)
        txn_dict = self.contract.functions.updateMetadata(tokenId, new_url).build_transaction({
            'chainId': 534351,
            'gas': 140000,
            'gasPrice': self.w3.to_wei('1', 'gwei'),
            'nonce': nonce,
        })
        signed_txn = self.w3.eth.account.sign_transaction(txn_dict, self.pk)
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return tx_hash
    