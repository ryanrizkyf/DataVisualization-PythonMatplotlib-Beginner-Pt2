# Bagaimana dengan customer kita di DKI Jakarta? Apakah ada pola-pola menarik, terutama di Q4 2019?
# Untuk itu, coba kita lihat dulu summary untuk tiap customer

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

# buat dataframe baru bernama data_per_customer_dki_q4.
data_per_customer = (dataset_dki_q4.groupby('customer_id')
                                   .agg({'order_id': 'nunique',
                                         'quantity': 'sum',
                                         'gmv': 'sum'})
                                   .reset_index()
                                   .rename(columns={'order_id': 'orders'}))
print(data_per_customer.sort_values(by='orders', ascending=False))

# Di sini menggunakan function agg untuk melakukan agregasi data.
# Data agregat per customer yang diambil yaitu jumlah orders (banyaknya unique order_id),
# total quantity, dan total GMV.

# Lalu didapatkan 711 customers yang bertransaksi di DKI Jakarta pada Q4 2020.

# Jika diurutkan dari jumlah order terbanyak, bisa dilihat bahwa customer_id 12748
# telah melakukan 29 transaksi dengan jumlah quantity mencapai 557, dan GMV lebih dari 175 Juta!
