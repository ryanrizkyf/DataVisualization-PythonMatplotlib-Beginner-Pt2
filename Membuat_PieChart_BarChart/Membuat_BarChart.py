# Alternatif lain untuk membandingkan GMV tiap kota adalah dengan barchart.
# Bar Chart lebih enak pas untuk visualisasi ini karena lebih mudah terlihat perbandingan antar kota

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

# Syntax dalam praktik membuat bar chart mirip dengan line chart, tentukan nilai untuk sumbu-x dan sumbu-y,
# lalu tambahkan parameter kind='bar'
plt.clf()
dataset_dki_q4.groupby('city')['gmv'].sum().sort_values(
    ascending=False).plot(kind='bar', color='green')
plt.title('GMV Per City - DKI Jakarta in Q4 2019',
          loc='center', pad=30, fontsize=15, color='blue')
plt.xlabel('City', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.xticks(rotation=0)
plt.show()

# Perhatikan di sini juga ditambahkan parameter rotation di plt.xtick() untuk memutar label di sumbu-x.

# Sebagai catatan, jika ingin barchart-nya horizontal, maka bisa mengganti parameternya menjadi kind='barh',
# dengan tentu saja tidak lupa juga harus menyesuaikan sumbu x dan y nya.
