import pandas as pd
import matplotlib.pyplot as plt

# Load data
penjualan_df = pd.read_csv('penjualan.csv')
persediaan_df = pd.read_csv('persediaan.csv')

# Filter data produk A dari penjualan
produk_a_penjualan = penjualan_df[penjualan_df['Produk'] == 'Produk A']

# Filter data produk A dari persediaan
produk_a_persediaan = persediaan_df[persediaan_df['Nama Barang'] == 'Produk A']

# Plot penjualan produk A
plt.figure(figsize=(10, 6))
plt.plot(produk_a_penjualan['Tanggal'], produk_a_penjualan['Jumlah'], marker='o', linestyle='-')
plt.title('Tren Penjualan Produk A')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penjualan')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot persediaan produk A
plt.figure(figsize=(10, 6))
plt.plot(produk_a_persediaan['Kode Barang'], produk_a_persediaan['Stok Akhir'], marker='o', linestyle='-')
plt.title('Tren Persediaan Produk A')
plt.xlabel('Kode Barang')
plt.ylabel('Stok Akhir')
plt.grid(True)
plt.tight_layout()
plt.show()
