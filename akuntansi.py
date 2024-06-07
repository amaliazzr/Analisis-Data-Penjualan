import csv

# Tabel 1: Penjualan
penjualan_data = [
    ["Tanggal", "No. Faktur", "Kode Pelanggan", "Nama Pelanggan", "Produk", "Jumlah", "Harga Satuan", "Total"],
    ["2024-01-03", "INV001", "P001", "PT Alpha", "Produk A", 50, 200000, 10000000],
    ["2024-01-05", "INV002", "P002", "PT Beta", "Produk B", 30, 150000, 4500000],
    ["2024-01-10", "INV003", "P003", "PT Gamma", "Produk C", 40, 100000, 4000000],
    ["2024-01-15", "INV004", "P004", "PT Delta", "Produk D", 25, 250000, 6250000],
    ["2024-01-20", "INV005", "P005", "PT Epsilon", "Produk A", 60, 200000, 12000000],
    ["2024-02-02", "INV006", "P006", "PT Zeta", "Produk B", 35, 150000, 5250000],
    ["2024-02-10", "INV007", "P007", "PT Eta", "Produk C", 45, 100000, 4500000],
    ["2024-02-18", "INV008", "P008", "PT Theta", "Produk D", 30, 250000, 7500000],
    ["2024-03-05", "INV009", "P009", "PT Iota", "Produk A", 55, 200000, 11000000],
    ["2024-03-10", "INV010", "P010", "PT Kappa", "Produk B", 25, 150000, 3750000]
]

# Tabel 2: Persediaan
persediaan_data = [
    ["Kode Barang", "Nama Barang", "Kategori", "Stok Awal", "Pembelian", "Penjualan", "Stok Akhir"],
    ["B001", "Produk A", "Elektronik", 100, 50, 60, 90],
    ["B002", "Produk B", "Elektronik", 200, 30, 40, 190],
    ["B003", "Produk C", "Elektronik", 150, 40, 45, 145],
    ["B004", "Produk D", "Elektronik", 80, 25, 35, 70],
    ["B005", "Produk E", "Elektronik", 120, 60, 50, 130],
    ["B006", "Produk F", "Elektronik", 90, 35, 30, 95],
    ["B007", "Produk G", "Elektronik", 110, 45, 40, 115],
    ["B008", "Produk H", "Elektronik", 130, 50, 55, 125],
    ["B009", "Produk I", "Elektronik", 170, 55, 60, 165],
    ["B010", "Produk J", "Elektronik", 140, 60, 65, 135]
]

# Tabel 3: Pembelian
pembelian_data = [
    ["Tanggal", "No. Faktur", "Kode Supplier", "Nama Supplier", "Produk", "Jumlah", "Harga Satuan", "Total"],
    ["2024-01-04", "PO001", "S001", "PT Lambda", "Produk A", 50, 180000, 9000000],
    ["2024-01-08", "PO002", "S002", "PT Mu", "Produk B", 30, 140000, 4200000],
    ["2024-01-12", "PO003", "S003", "PT Nu", "Produk C", 40, 90000, 3600000],
    ["2024-01-18", "PO004", "S004", "PT Xi", "Produk D", 25, 230000, 5750000],
    ["2024-01-22", "PO005", "S005", "PT Omicron", "Produk E", 60, 190000, 11400000],
    ["2024-02-04", "PO006", "S006", "PT Pi", "Produk F", 35, 160000, 5600000],
    ["2024-02-12", "PO007", "S007", "PT Rho", "Produk G", 45, 170000, 7650000],
    ["2024-02-20", "PO008", "S008", "PT Sigma", "Produk H", 30, 150000, 4500000],
    ["2024-03-06", "PO009", "S009", "PT Tau", "Produk I", 55, 200000, 11000000],
    ["2024-03-12", "PO010", "S010", "PT Upsilon", "Produk J", 25, 220000, 5500000]
]

# Tabel 4: Beban Operasional
beban_operasional_data = [
    ["Tanggal", "Kategori", "Deskripsi", "Jumlah", "Harga Satuan", "Total"],
    ["2024-01-07", "Gaji Karyawan", "Gaji Bulanan", 10, 5000000, 50000000],
    ["2024-01-14", "Listrik", "Biaya Listrik", 1, 3000000, 3000000],
    ["2024-01-21", "Sewa Gedung", "Sewa Bulanan", 1, 10000000, 10000000],
    ["2024-01-28", "Transportasi", "Biaya Transportasi", 1, 2500000, 2500000],
    ["2024-02-04", "Gaji Karyawan", "Gaji Bulanan", 10, 5000000, 50000000],
    ["2024-02-11", "Listrik", "Biaya Listrik", 1, 3000000, 3000000],
    ["2024-02-18", "Sewa Gedung", "Sewa Bulanan", 1, 10000000, 10000000],
    ["2024-02-25", "Transportasi", "Biaya Transportasi", 1, 2500000, 2500000],
    ["2024-03-07", "Gaji Karyawan", "Gaji Bulanan", 10, 5000000, 50000000],
    ["2024-03-14", "Listrik", "Biaya Listrik", 1, 3000000, 3000000]
]

# Tabel 5: Piutang Usaha
piutang_usaha_data = [
    ["Tanggal", "No. Faktur", "Kode Pelanggan", "Nama Pelanggan", "Jumlah Piutang", "Tanggal Jatuh Tempo", "Status"],
    ["2024-01-03", "INV001", "P001", "PT Alpha", 10000000, "2024-01-31", "Belum Lunas"],
    ["2024-01-05", "INV002", "P002", "PT Beta", 4500000, "2024-02-04", "Belum Lunas"],
    ["2024-01-10", "INV003", "P003", "PT Gamma", 4000000, "2024-02-09", "Belum Lunas"],
    ["2024-01-15", "INV004", "P004", "PT Delta", 6250000, "2024-02-14", "Belum Lunas"],
    ["2024-01-20", "INV005", "P005", "PT Epsilon", 12000000, "2024-02-19", "Belum Lunas"],
    ["2024-02-02", "INV006", "P006", "PT Zeta", 5250000, "2024-03-03", "Belum Lunas"],
    ["2024-02-10", "INV007", "P007", "PT Eta", 4500000, "2024-03-11", "Belum Lunas"],
    ["2024-02-18", "INV008", "P008", "PT Theta", 7500000, "2024-03-19", "Belum Lunas"],
    ["2024-03-05", "INV009", "P009", "PT Iota", 11000000, "2024-04-04", "Belum Lunas"],
    ["2024-03-10", "INV010", "P010", "PT Kappa", 3750000, "2024-04-09", "Belum Lunas"]
]

# Simpan data ke dalam file CSV
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

# Simpan data ke dalam file CSV
save_to_csv(penjualan_data, 'penjualan.csv')
save_to_csv(persediaan_data, 'persediaan.csv')
save_to_csv(pembelian_data, 'pembelian.csv')
save_to_csv(beban_operasional_data, 'beban_operasional.csv')
save_to_csv(piutang_usaha_data, 'piutang_usaha.csv')

print("Data telah disimpan dalam format CSV.")
