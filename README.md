

# 🚀 Auto Transaction EVM

Script Python untuk mengirim transaksi ke banyak alamat secara otomatis di jaringan EVM (Ethereum, BSC, Arbitrum, Polygon, dll).

---

## 📦 Persiapan

1. **Clone repository**
   ```bash
   git clone https://github.com/0xvans/autotransactionEVM
   cd autotransactionEVM
Install dependencies

pip install web3 python-dotenv
pip install -r requirements.txt
Buat file .env
Di dalam root project, buat file .env lalu isi dengan data berikut:

PRIVATE_KEY=0xyourprivatekey
RPC_URL=https://your-rpc-url
CHAIN_ID=1
PRIVATE_KEY → private key wallet (gunakan wallet dummy/testnet dulu).

RPC_URL → RPC provider (misalnya Alchemy, Infura, atau node pribadi).

CHAIN_ID → chain id (Ethereum Mainnet = 1, Goerli = 5, BSC = 56, Polygon = 137, dll).

📂 File Konfigurasi
1. Daftar Alamat Tujuan
Buat file recipients.txt berisi daftar alamat tujuan, 1 per baris.
Contoh:

0x1234567890abcdef1234567890abcdef12345678,0.01
0xabcdefabcdefabcdefabcdefabcdefabcdefabcd,0.05
Format:

alamat_wallet,jumlah_eth
2. Script Utama (send_many.py)
Script ini akan membaca file recipients.txt, lalu mengirim ETH/token sesuai jumlah yang ditentukan.

▶️ Cara Menjalankan
Jalankan perintah:

python send_many.py
Jika berhasil, terminal akan menampilkan hash transaksi untuk setiap pengiriman.

🛠️ Contoh Alur Lengkap
Clone repo:

git clone https://github.com/0xvans/autotransactionEVM
cd autotransactionEVM
Install requirements:

pip install -r requirements.txt
Buat file .env:

PRIVATE_KEY=0xabc123...xyz
RPC_URL=https://eth-sepolia.g.alchemy.com/v2/your_api_key
CHAIN_ID=11155111
Buat file recipients.txt:

0xaaa1111111111111111111111111111111111111,0.01
0xbbb2222222222222222222222222222222222222,0.02
Jalankan script:

python send_many.py
Lihat hasil di explorer (Etherscan, BscScan, PolygonScan, dll).
