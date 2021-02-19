# Dari dataframe baru ini kita bisa melihat persebaran datanya sekaligus untuk masing-masing variabel.
# Jadi, kita perlu untuk memakai  histogram

# Dapat menggunakan function plt.hist dan memasukkan variabel yang ingin dicek.
# Parameter lain yang bisa ditambahkan yaitu:
# 1. bins: jumlah bin (kelompok nilai) yang diinginkan
# 2. range: nilai minimum dan maksimum yang ditampilkan
# 3. orientation: ‘horizontal’ atau ‘vertikal’
# 4. color: warna bar di histogram

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


# Mulai dari variabel orders, dimulai tanpa parameter apapun.
plt.clf()
# Histogram pertama
plt.figure()
plt.hist(data_per_customer['orders'])
plt.show()

# Terlihat bahwa datanya terlalu berat ke kiri, hampir semua customer hanya bertransaksi kurang dari 10,
# maka dari itu perlu set range-nya, misalnya hanya dari 1 sampai 5.
# Histogram kedua
plt.figure()
plt.hist(data_per_customer['orders'], range=(1, 5))
plt.title('Distribution of Number of Orders per Customer\nDKI Jakarta in Q4 2019',
          fontsize=15, color='blue')
plt.xlabel('Number of Orders', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.show()
