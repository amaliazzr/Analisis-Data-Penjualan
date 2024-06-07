import pandas as pd
import matplotlib.pyplot as plt

# Load data
pembelian_df = pd.read_csv('pembelian.csv')

# Parse tanggal sebagai datetime
pembelian_df['Tanggal'] = pd.to_datetime(pembelian_df['Tanggal'])

# Ekstrak bulan dari tanggal
pembelian_df['Bulan'] = pembelian_df['Tanggal'].dt.strftime('%Y-%m')

# Hitung total pembelian per bulan
total_pembelian_per_bulan = pembelian_df.groupby('Bulan')['Total'].sum().reset_index()

# Plot distribusi pembelian per bulan
plt.figure(figsize=(10, 6))
plt.bar(total_pembelian_per_bulan['Bulan'], total_pembelian_per_bulan['Total'], color='skyblue')
plt.title('Distribusi Pembelian per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Pembelian (IDR)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Analisis pola pembelian dari supplier
pembelian_per_supplier = pembelian_df.groupby('Nama Supplier')['Total'].sum().reset_index()

# Plot pola pembelian dari supplier
plt.figure(figsize=(10, 6))
plt.barh(pembelian_per_supplier['Nama Supplier'], pembelian_per_supplier['Total'], color='salmon')
plt.title('Pola Pembelian dari Supplier')
plt.xlabel('Total Pembelian (IDR)')
plt.ylabel('Nama Supplier')
plt.grid(axis='x')
plt.tight_layout()
plt.show()
