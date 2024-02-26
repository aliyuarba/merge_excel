
import os
import pandas as pd

# Tentukan folder tempat berada file-file Excel
folder_path = '.\SSH'

# Buat list kosong untuk menyimpan DataFrame dari setiap file
data_frames = []

# Loop melalui setiap file dalam folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        # Membaca file Excel
        file_path = os.path.join(folder_path, filename)
        df = pd.read_excel(file_path)
        
        # Menambahkan DataFrame ke list
        data_frames.append(df)

# Menggabungkan semua DataFrame dalam list menjadi satu
merged_data = pd.concat(data_frames, ignore_index=True)

# Menyimpan hasil penggabungan ke file Excel baru
merged_data.to_excel('hasil_gabungan.xlsx', index=False)

# print("10")