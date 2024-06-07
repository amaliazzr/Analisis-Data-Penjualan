import pandas as pd
import matplotlib.pyplot as plt

# Load data
penjualan_df = pd.read_csv('penjualan.csv')
pembelian_df = pd.read_csv('pembelian.csv')

# Hitung total penjualan per produk
total_penjualan_per_produk = penjualan_df.groupby('Produk')['Total'].sum().reset_index()

# Hitung total pembelian per produk
total_pembelian_per_produk = pembelian_df.groupby('Produk')['Total'].sum().reset_index()

# Gabungkan data penjualan dan pembelian
merged_df = pd.merge(total_penjualan_per_produk, total_pembelian_per_produk, on='Produk', suffixes=('_penjualan', '_pembelian'))

# Hitung marjin keuntungan bersih
merged_df['Marjin Keuntungan Bersih'] = merged_df['Total_penjualan'] - merged_df['Total_pembelian']

# Plot marjin keuntungan bersih per produk
plt.figure(figsize=(10, 6))
plt.bar(merged_df['Produk'], merged_df['Marjin Keuntungan Bersih'], color='skyblue')
plt.title('Marjin Keuntungan Bersih per Produk')
plt.xlabel('Produk')
plt.ylabel('Marjin Keuntungan Bersih (IDR)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Tentukan produk yang memberikan kontribusi terbesar terhadap laba bersih
produk_terbaik = merged_df.loc[merged_df['Marjin Keuntungan Bersih'].idxmax()]

print("Produk yang memberikan kontribusi terbesar terhadap laba bersih per bulan adalah:", produk_terbaik['Produk'])
print("Dengan marjin keuntungan bersih sebesar:", produk_terbaik['Marjin Keuntungan Bersih'])
