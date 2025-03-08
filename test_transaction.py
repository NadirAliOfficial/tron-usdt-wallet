from tronpy import Tron
from tronpy.keys import PrivateKey

# Connect to the Tron Shasta testnet
client = Tron(network='shasta')

# Your funded test wallet details:
# Replace with your private key (hex string, without a '0x' prefix) from your test wallet.
sender_private_key = PrivateKey(bytes.fromhex("2f60abed403a9a68426fe106774dd8f19f91ed1e1b8534d12a970c0911ffdeb3"))
sender_address = sender_private_key.public_key.to_base58check_address()

# Destination address for the transaction (another test wallet)
destination_address = "THa1zYpEuCW26Syav3kjxV5jwdv32WmcMh"

# Define the transfer amount in Sun (1 TRX = 1,000,000 Sun)
amount_in_sun = 1_000_000  

# Build the transfer transaction
txn = (
    client.trx.transfer(sender_address, destination_address, amount_in_sun)
    .build()
)

# Sign the transaction with the sender's private key
signed_txn = txn.sign(sender_private_key)

# Broadcast the transaction to the network
result = signed_txn.broadcast()

print("Transaction broadcast result:")
print(result)
