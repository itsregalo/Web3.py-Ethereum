from web3 import Web3
from decouple import config

# Connect to Ethereum network using an Ethereum node URL
w3 = Web3(Web3.HTTPProvider(config('ethereum_infura_endpoint')))

# Create a new Ethereum wallet
wallet = w3.eth.account.create()

# Print the wallet details
print('Private key:', wallet._private_key.hex())
# print('Public key:', wallet._public_key.hex())
print('Address:', wallet._address)

# Write the wallet details to a file
with open('wallet.txt', 'w') as f:
    f.write('Private key: ' + wallet._private_key.hex() + '\n')
    # f.write('Public key: ' + wallet.publicKey.hex() + '\n')
    f.write('Ethereum address: ' + wallet.address)
