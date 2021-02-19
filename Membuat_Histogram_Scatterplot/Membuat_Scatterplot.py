# Untuk membuat scatterplot, perlu menggunakan function plt.scatter
# dengan memasukkan variabel-variabel yang akan dibuat scatterplot.

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

# untuk melihat scatterplot quantity vs GMV
plt.clf()
# Scatterplot pertama
plt.figure()
plt.scatter(data_per_customer['quantity'], data_per_customer['gmv'])
plt.show()

# Terlihat bahwa memang semakin besar quantity-nya, GMV cenderung semakin tinggi.
# Tapi masalahnya datanya banyak terkumpul di nilai-nilai kecil,
# sehingga tidak begitu terlihat detailnya di area situ.
# Scatterplot kedua: perbaikan scatterplot pertama
plt.figure(figsize=(10, 8))
plt.scatter(data_per_customer['quantity'],
            data_per_customer['gmv'], marker='+', color='red')
plt.title('Correlation of Quantity and GMV per Customer\nDKI Jakarta in Q4 2019',
          fontsize=15, color='blue')
plt.xlabel('Quantity', fontsize=12)
plt.ylabel('GMV (in Millions)', fontsize=12)
plt.xlim(xmin=0, xmax=300)
plt.ylim(ymin=0, ymax=150000000)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000).astype(int))
plt.show()

# Di sini semakin jelas bahwa quantity dan GMV itu berkorelasi positif.
# Jadi jika suatu customer telah membeli dengan banyak quantity,
# maka kemungkinan GMV dari dia juga semakin besar.
