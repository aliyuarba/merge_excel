import os
import pandas as pd

# Tentukan folder tempat berada file-file Excel
folder_path = '.\SSH'

# Buat list kosong untuk menyimpan DataFrame dari setiap file
data_frames = []

# Buat dictionary untuk menyimpan jumlah baris untuk masing-masing file
jumlah_baris_dict = {}

# Loop melalui setiap file dalam folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        # Membaca file Excel
        file_path = os.path.join(folder_path, filename)
        df = pd.read_excel(file_path)
        
        # Menambahkan DataFrame ke list
        data_frames.append(df)
        
        # Menyimpan jumlah baris untuk file tertentu
        jumlah_baris_dict[filename] = len(df)

# Menggabungkan semua DataFrame dalam list menjadi satu
merged_data = pd.concat(data_frames, ignore_index=True)

# Menyimpan hasil penggabungan ke file Excel baru
merged_data.to_excel('gabung_SSH.xlsx', index=False)

# Menampilkan jumlah file yang berhasil tergabung
print(f"Jumlah file yang berhasil tergabung: {len(data_frames)}")

# Menampilkan jumlah baris untuk masing-masing file
for filename, jumlah_baris in jumlah_baris_dict.items():
    print(f"File: {filename}, Jumlah Baris: {jumlah_baris}")

# Menampilkan jumlah baris keseluruhan
total_jumlah_baris = len(merged_data)
print(f"Jumlah Baris Keseluruhan: {total_jumlah_baris}")
