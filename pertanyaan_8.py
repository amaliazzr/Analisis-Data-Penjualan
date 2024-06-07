import pandas as pd
import matplotlib.pyplot as plt

# Load data
penjualan_df = pd.read_csv('penjualan.csv')

# Parse tanggal sebagai datetime
penjualan_df['Tanggal'] = pd.to_datetime(penjualan_df['Tanggal'])

# Ekstrak bulan dari tanggal
penjualan_df['Bulan'] = penjualan_df['Tanggal'].dt.strftime('%Y-%m')

# Hitung total penjualan per bulan
total_penjualan_per_bulan = penjualan_df.groupby('Bulan')['Total'].sum().reset_index()

# Buat kolom untuk menyimpan proyeksi
proyeksi_df = total_penjualan_per_bulan.copy()

# Menggunakan metode moving average untuk membuat proyeksi
proyeksi_df['Proyeksi'] = proyeksi_df['Total'].rolling(window=3).mean()

# Plot data historis dan proyeksi
plt.figure(figsize=(10, 6))
plt.plot(proyeksi_df['Bulan'], proyeksi_df['Total'], marker='o', linestyle='-', label='Data Historis')
plt.plot(proyeksi_df['Bulan'], proyeksi_df['Proyeksi'], marker='o', linestyle='-', color='red', label='Proyeksi')
plt.title('Proyeksi Keuangan Berdasarkan Tren Historis')
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan (IDR)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
