# kita ubah multi-bar chart sebelumnya menjadi stacked barchart

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

# untuk membuat stacked chart
dataset_dki_q4.groupby(['order_month', 'city'])['gmv'].sum().sort_values(
    ascending=False).unstack().plot(kind='bar', stacked=True)
plt.title('GMV Per Month, Breakdown by City\nDKI Jakarta in Q4 2019',
          loc='center', pad=30, fontsize=15, color='blue')
plt.xlabel('Order Month', fontsize=12)
plt.ylabel('Total Amount (in Billions)', fontsize=12)
plt.legend(bbox_to_anchor=(1, 1), shadow=True, ncol=1, title='City')
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Dari kedua chart tersebut, kita sama-sama bisa melihat pola bahwa kebanyakan GMV
# turun dari bulan Oktober ke November, tetapi lalu naik pesat di bulan Desember.
# Untuk di Jakarta Barat, GMV November justru naik dari Oktober. Sedangkan di Jakarta Selatan,
# GMV Desember justru lebih kecil daripada GMV Oktober
