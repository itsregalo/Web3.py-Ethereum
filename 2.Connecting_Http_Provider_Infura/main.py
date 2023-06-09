from web3 import Web3
from decouple import config
# using a remote node

w3 = Web3(Web3.HTTPProvider(config('ethereum_infura_endpoint')))

# Check if connected to Ethereum node
print(w3.is_connected())
