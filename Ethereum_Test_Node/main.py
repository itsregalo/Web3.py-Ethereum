from web3 import Web3

# Connect to local Ethereum node
from web3 import EthereumTesterProvider

# Connect to local Ethereum node
w3 = Web3(EthereumTesterProvider())

# Check if connected to Ethereum node
print(w3.is_connected())