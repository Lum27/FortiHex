from web3 import Web3 

# Connect to a local Ethereum node (Ganache)
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Read contract data
with open("SecurityLog.sol", "r") as f:
    contract_source_code = f.read()

# Complie contract using solcx
from solcx import complie_source
compiled_sol = complie_source(contract_source_code)
contract_interface = compiled_sol["<stdin>:SecurityLog"]

# Deploy contract
contract = web3.eth.contract(abi=contract_interface["abi"], bytecode=contract_interface["bin"])
tx_hash = contract.constructor().transact({"from": web3.eth.accounts[0]})
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Deployed SecurityLog at {tx_receipt.contractAddress}")