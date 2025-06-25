from web3 import Web3
from dotenv import load_dotenv
import os
import time

# Load konfigurasi dari .env
load_dotenv()
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
RPC_URL = os.getenv("RPC_URL")
WALLET_ADDRESS = Web3.to_checksum_address(os.getenv("WALLET_ADDRESS"))

# Setup koneksi Web3
w3 = Web3(Web3.HTTPProvider(RPC_URL))
assert w3.is_connected(), "Gagal konek ke RPC"

# Fungsi untuk mengirim ETH
def send_transaction(to_address, amount_eth, nonce):
    tx = {
        'nonce': nonce,
        'to': Web3.to_checksum_address(to_address),
        'value': w3.to_wei(amount_eth, 'ether'),
        'gas': 21000,
        'gasPrice': w3.eth.gas_price,
        'chainId': w3.eth.chain_id,
    }

    signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return w3.to_hex(tx_hash)

# Baca file address
with open('address_list.txt') as f:
    address_list = [line.strip().split(',') for line in f if line.strip()]

# Dapatkan nonce awal
start_nonce = w3.eth.get_transaction_count(WALLET_ADDRESS)

# Loop pengiriman
for i, (to, amount) in enumerate(address_list):
    try:
        tx_hash = send_transaction(to, float(amount), start_nonce + i)
        print(f"{i+1}. Sent {amount} ETH to {to} | TX: {tx_hash}")
        time.sleep(0.5)  # delay sedikit agar stabil
    except Exception as e:
        print(f"{i+1}. Gagal kirim ke {to}: {e}")
