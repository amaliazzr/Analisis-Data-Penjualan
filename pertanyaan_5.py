import pandas as pd
import matplotlib.pyplot as plt

# Load data
penjualan_df = pd.read_csv('penjualan.csv')
pembelian_df = pd.read_csv('pembelian.csv')
beban_operasional_df = pd.read_csv('beban_operasional.csv')

# Parse tanggal sebagai datetime
penjualan_df['Tanggal'] = pd.to_datetime(penjualan_df['Tanggal'])
pembelian_df['Tanggal'] = pd.to_datetime(pembelian_df['Tanggal'])
beban_operasional_df['Tanggal'] = pd.to_datetime(beban_operasional_df['Tanggal'])

# Ekstrak bulan dari tanggal
penjualan_df['Bulan'] = penjualan_df['Tanggal'].dt.strftime('%Y-%m')
pembelian_df['Bulan'] = pembelian_df['Tanggal'].dt.strftime('%Y-%m')
beban_operasional_df['Bulan'] = beban_operasional_df['Tanggal'].dt.strftime('%Y-%m')

# Hitung total pendapatan per bulan
total_pendapatan_per_bulan = penjualan_df.groupby('Bulan')['Total'].sum().reset_index()

# Hitung total pembelian per bulan
total_pembelian_per_bulan = pembelian_df.groupby('Bulan')['Total'].sum().reset_index()

# Hitung total biaya operasional per bulan
total_beban_per_bulan = beban_operasional_df.groupby('Bulan')['Total'].sum().reset_index()

# Gabungkan data total pendapatan, pembelian, dan biaya operasional
merged_df = pd.merge(total_pendapatan_per_bulan, total_pembelian_per_bulan, on='Bulan', how='outer')
merged_df = pd.merge(merged_df, total_beban_per_bulan, on='Bulan', how='outer')
merged_df = merged_df.fillna(0)
merged_df['Total Biaya Operasional'] = merged_df['Total'] + merged_df['Total_x']
merged_df['Laba Bersih'] = merged_df['Total_y'] - merged_df['Total Biaya Operasional']

# Plot tren keseluruhan
plt.figure(figsize=(10, 6))
plt.plot(merged_df['Bulan'], merged_df['Total'], marker='o', linestyle='-', label='Pendapatan')
plt.plot(merged_df['Bulan'], merged_df['Total_y'], marker='o', linestyle='-', label='Pembelian')
plt.plot(merged_df['Bulan'], merged_df['Total Biaya Operasional'], marker='o', linestyle='-', label='Biaya Operasional')
plt.plot(merged_df['Bulan'], merged_df['Laba Bersih'], marker='o', linestyle='-', label='Laba Bersih')
plt.title('Tren Keseluruhan')
plt.xlabel('Bulan')
plt.ylabel('Total (IDR)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
