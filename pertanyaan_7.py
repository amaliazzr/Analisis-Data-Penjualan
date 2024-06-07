import pandas as pd
import matplotlib.pyplot as plt

# Load data
beban_operasional_df = pd.read_csv('beban_operasional.csv')

# Parse tanggal sebagai datetime
beban_operasional_df['Tanggal'] = pd.to_datetime(beban_operasional_df['Tanggal'])

# Ekstrak bulan dari tanggal
beban_operasional_df['Bulan'] = beban_operasional_df['Tanggal'].dt.strftime('%Y-%m')

# Hitung total biaya operasional per bulan dan kategori
total_beban_per_bulan_kategori = beban_operasional_df.groupby(['Bulan', 'Kategori'])['Total'].sum().reset_index()

# Pivot tabel untuk membuat data lebih mudah diinterpretasikan
pivot_table = total_beban_per_bulan_kategori.pivot(index='Bulan', columns='Kategori', values='Total').fillna(0)

# Plot perbandingan biaya operasional per kategori dari bulan ke bulan
plt.figure(figsize=(12, 8))
pivot_table.plot(kind='bar', stacked=True)
plt.title('Perbandingan Biaya Operasional per Kategori dari Bulan ke Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Biaya Operasional (IDR)')
plt.xticks(rotation=45)
plt.legend(title='Kategori')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Analisis kategori biaya operasional yang meningkat secara signifikan dari bulan ke bulan
monthly_change = pivot_table.pct_change().dropna()
significant_increase = monthly_change[monthly_change > 0.1].dropna(axis=1)

if len(significant_increase.columns) > 0:
    print("Kategori biaya operasional yang mengalami peningkatan signifikan (>10%) dari bulan ke bulan:")
    print(significant_increase.columns)
else:
    print("Tidak ada kategori biaya operasional yang mengalami peningkatan signifikan (>10%) dari bulan ke bulan.")

# Strategi untuk mengoptimalkan biaya operasional dan meningkatkan efisiensi
print("\nStrategi untuk mengoptimalkan biaya operasional dan meningkatkan efisiensi:")
print("- Melakukan audit terhadap pengeluaran di kategori biaya operasional yang mengalami peningkatan signifikan.")
print("- Mencari alternatif penyedia atau negosiasi ulang kontrak dengan pemasok untuk mendapatkan harga yang lebih baik.")
print("- Menerapkan kebijakan penghematan, seperti mengurangi konsumsi listrik atau memperbaiki efisiensi logistik.")
