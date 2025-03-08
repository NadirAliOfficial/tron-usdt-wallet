# Tron Wallet Tester

This repository provides scripts to create a Tron wallet and test transactions on the Tron network using the [Tronpy](https://github.com/andelf/tronpy) Python library. It is designed for development and testing on the Tron Shasta testnet.

## Features

- **Create a New Wallet:**  
  Generate a secure, random Tron wallet with a private key and public address.

- **Test Transactions:**  
  Build, sign, and broadcast TRX transactions on the Shasta testnet to simulate real-world usage without risking real funds.

- **Extendable Code:**  
  Easily extend the scripts for TRC20 token transfers or other Tron blockchain interactions.

## Prerequisites

- Python 3.6 or later.
- [Tronpy](https://github.com/andelf/tronpy) library.
- A funded test account on the Tron Shasta testnet.  
  *(Get test TRX from a [Shasta Faucet](https://www.trongrid.io/shasta) or similar service.)*

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/NadirAliOfficial/tron-usdt-wallet
   cd tron-usdt-wallet
   ```

2. **(Optional) Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages:**

   ```bash
   pip install tronpy
   ```

## Usage

### Create a New Tron Wallet

Create a file named `create_wallet.py` with the following content:

```python
from tronpy.keys import PrivateKey

# Generate a random private key
private_key = PrivateKey.random()

# Derive the public address in Base58Check format
wallet_address = private_key.public_key.to_base58check_address()

print("New Tron Wallet Created!")
print("Wallet Address:", wallet_address)
print("Private Key:", private_key.hex())
```

Run the script:

```bash
python create_wallet.py
```

### Test a Transaction on the Tron Shasta Testnet

Create a file named `test_transaction.py` with the following content. Replace the placeholder values with your actual test account details:

```python
from tronpy import Tron
from tronpy.keys import PrivateKey

# Connect to the Tron Shasta testnet
client = Tron(network='shasta')

# Your funded test wallet details:
# Replace with your private key (hex string, without a '0x' prefix) from your test wallet.
sender_private_key = PrivateKey(bytes.fromhex("YOUR_PRIVATE_KEY"))
sender_address = sender_private_key.public_key.to_base58check_address()

# Destination address for the transaction (another test wallet)
destination_address = "DESTINATION_ADDRESS"

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
```

Run the script:

```bash
python test_transaction.py
```

After running the transaction script, you can verify the transaction using a Tron testnet explorer such as [Shasta Explorer](https://shasta.tronscan.org/).

## Security Notice

- **Private Key Management:**  
  Never expose your private key publicly or commit it to version control. For production, use environment variables or secure key management solutions.

- **Testnet Only:**  
  Always test on the Shasta testnet before moving any code or transactions to the mainnet.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for enhancements or additional features.

## License

This project is licensed under the MIT License.
