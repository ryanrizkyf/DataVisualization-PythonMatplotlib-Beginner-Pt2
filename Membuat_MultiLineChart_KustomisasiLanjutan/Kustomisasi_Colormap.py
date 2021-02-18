# Kalau sudah di breakdown by brand seperti ini terlihat ya trend sepanjang Oktober-Desember 2019
# ini mirip semua. Jadi kemungkinan tidak ada faktor dari brand yang membuat GMV kita naik.
# Selanjutnya, perlihatkan data breakdown by province,

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

plt.clf()
dataset.groupby(['order_month', 'province'])[
    'gmv'].sum().unstack().plot(cmap='Set1')
plt.title('Monthly GMV Year 2019 - Breakdown by Province',
          loc='center', pad=30, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.5), shadow=True,
           ncol=3, title='Province', fontsize=9, title_fontsize=11)
plt.gcf().set_size_inches(10, 5)
plt.tight_layout()
plt.show()

# Selain itu, perhatikan juga bahwa pada grafik tersebut, list warnanya berbeda,
# tidak default seperti pada brand. Itu karena di function plot()
# ditambahkan parameter cmap (yakni, color map) yang mendefinisikan sekelompok warna
# yang akan diberikan untuk tiap line. Di sini yang digunakan adalah ‘Set1’,
# yakni satu set warna yang biasa digunakan untuk warna yang diskrit.
# Untuk mengetahui jenis-jenis color map, bisa dilihat di halaman
# web berikut: https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html.

# Dari grafik ini, terlihat ada beberapa provinsi yang mendominasi kenaikan GMV,
# seperti DKI Jakarta dan Jawa Barat. Tapi karena provinsinya banyak, yang bawah-bawah jadi kurang jelasnya.
# Bercampur semua begitu garisnya.
