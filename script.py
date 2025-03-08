from tronpy.keys import PrivateKey

# Generate a random private key
private_key = PrivateKey.random()

# Derive the public address in Base58Check format
wallet_address = private_key.public_key.to_base58check_address()

print("New Tron Wallet Created!")
print("Wallet Address:", wallet_address)
print("Private Key:", private_key.hex())
