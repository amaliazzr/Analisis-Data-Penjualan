import pandas as pd
import matplotlib.pyplot as plt

# Load data
piutang_usaha_df = pd.read_csv('piutang_usaha.csv')

# Analisis jumlah piutang dari setiap pelanggan
total_piutang_per_pelanggan = piutang_usaha_df.groupby('Nama Pelanggan')['Jumlah Piutang'].sum().reset_index()

# Plot jumlah piutang dari setiap pelanggan
plt.figure(figsize=(10, 6))
plt.bar(total_piutang_per_pelanggan['Nama Pelanggan'], total_piutang_per_pelanggan['Jumlah Piutang'], color='orange')
plt.title('Jumlah Piutang dari Setiap Pelanggan')
plt.xlabel('Nama Pelanggan')
plt.ylabel('Jumlah Piutang (IDR)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Analisis pelanggan yang cenderung membayar keterlambatan
status_piutang = piutang_usaha_df.groupby('Status').size()
labels = status_piutang.index
sizes = status_piutang.values

# Plot persentase status piutang
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
plt.title('Persentase Status Piutang')
plt.axis('equal')
plt.tight_layout()
plt.show()
