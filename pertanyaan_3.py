import pandas as pd
import matplotlib.pyplot as plt

# Load data
beban_operasional_df = pd.read_csv('beban_operasional.csv')

# Parse tanggal sebagai datetime
beban_operasional_df['Tanggal'] = pd.to_datetime(beban_operasional_df['Tanggal'])

# Ekstrak bulan dari tanggal
beban_operasional_df['Bulan'] = beban_operasional_df['Tanggal'].dt.strftime('%Y-%m')

# Hitung total biaya operasional per bulan
total_beban_per_bulan = beban_operasional_df.groupby('Bulan')['Total'].sum().reset_index()

# Plot perbandingan biaya operasional per bulan
plt.figure(figsize=(10, 6))
plt.plot(total_beban_per_bulan['Bulan'], total_beban_per_bulan['Total'], marker='o', linestyle='-')
plt.title('Perbandingan Biaya Operasional per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Biaya Operasional (IDR)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Analisis kategori biaya operasional yang paling berpengaruh
kategori_beban = beban_operasional_df.groupby('Kategori')['Total'].sum().reset_index()
kategori_beban_sorted = kategori_beban.sort_values(by='Total', ascending=False)

# Plot perbandingan kategori biaya operasional
plt.figure(figsize=(10, 6))
plt.bar(kategori_beban_sorted['Kategori'], kategori_beban_sorted['Total'], color='lightgreen')
plt.title('Perbandingan Kategori Biaya Operasional')
plt.xlabel('Kategori')
plt.ylabel('Total Biaya Operasional (IDR)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
