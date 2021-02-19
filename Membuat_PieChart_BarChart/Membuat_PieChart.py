# Sebelum membuat Pie Chart, kita perlu membuat dulu dataframe agregat

# Beberapa parameter yang bisa dimodifikasi:
# 1. labels: array yang berisikan label/tulisan yang ditunjukkan untuk masing-masing bagian pie.
# 2. colors: array yang berisikan warna untuk masing-masing bagian pie.
# 3. autopct: format untuk nilai persentasi yang ditampilkan, bisa berupa string atau function.
# 4. shadow: jika diisi True, maka ada bayangan untuk pie chart-nya. Defaultnya adalah False.
# 5. radius: jari-jari dari pie-chart

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

# Misalnya  gmv_per_city_dki_q4,  masukkan datanya ke function plt.pie().
gmv_per_city_dki_q4 = dataset_dki_q4.groupby('city')['gmv'].sum().reset_index()
plt.figure(figsize=(6, 6))
plt.pie(gmv_per_city_dki_q4['gmv'],
        labels=gmv_per_city_dki_q4['city'], autopct='%1.2f%%')
plt.title('GMV Contribution Per City - DKI Jakarta in Q4 2019',
          loc='center', pad=30, fontsize=15, color='blue')
plt.show()
