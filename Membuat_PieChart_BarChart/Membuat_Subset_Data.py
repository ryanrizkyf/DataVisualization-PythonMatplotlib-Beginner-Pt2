# Ada request kalau provinsi ‘other’ ini, kita analisis lagi di lain waktu saja dan
# fokuskan untuk analisis behavior transaksi di DKI Jakarta pada bulan Oktober-Desember 2019 ini,
# karena trend-nya mirip dengan overall GMV. Kita fokuskan ke sana ya,

# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv

# Import library
import datetime
import pandas as pd
import matplotlib.pyplot as plt
# Baca dataset
dataset = pd.read_csv(
    'retail_raw_reduced.csv')
# Buat kolom baru yang bertipe datetime dalam format '%Y-%m'
dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
# Buat Kolom GMV
dataset['gmv'] = dataset['item_price']*dataset['quantity']

# Berhubung kita mau fokus ke provinsi DKI Jakarta dan bulan Oktober-Desember 2019,
# kita filter saja datanya dan disimpan ke dataframe baru
dataset_dki_q4 = dataset[(dataset['province'] == 'DKI Jakarta') & (
    dataset['order_month'] >= '2019-10')]
print(dataset_dki_q4.head())
