# Kita punya komponen baru ya di sini, namanya legend.
# Berhubung brand-nya ada banyak, dan defaultnya di tengah makanya jadi menutupi grafiknya.
# Solusinya adalah kita pakai function khusus ya,

# Atur komponen legend menggunakan function plt.legend()

# Beberapa parameter yang bisa ditambahkan untuk legend:
# 1. loc: untuk menentukan posisi legend, berikut beberapa lokasi legend yang bisa didefinisikan:
# 'upper left', 'upper right', 'lower left', 'lower right':legend diletakkan di pojok dari axes
# (atas kiri, atas kanan, bawah kiri, atas kiri)
# 'upper center', 'lower center', 'center left', 'center right': legend diletakkan di tepi axes
# (atas tengah, bawah tengah, tengah kiri, tengah kanan)
# 'center': legend diletakkan di tengah-tengah axes
# 'best': matplotlib akan memilih satu dari sekian kemungkinan lokasi legend di atas yang paling
# tidak overlap dengan isi grafik
# 2. bbox_to_anchor: biasanya digunakan untuk adjust lokasi dari legend. Bisa berisi 2 angka yang
# menunjukkan koordinat x dan y (misal (1.6,0.5) berarti geser 1.6 ke kanan dan 0.5 ke atas).
# Bisa juga berisi 4 angka, angka ketiga dan keempat menyatakan width (lebar) dan height (tinggi) dari legend.
# 3. shadow: jika diisi True, maka kotak legend akan memiliki bayangan.
# 4. ncol: jumlah kolom dari isi legend, defaultnya adalah 1
# 5. fontsize: ukuran huruf pada legend
# 6. title: memberikan judul pada legend
# 7. title_fontsize: ukuran huruf pada judul legend

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

dataset.groupby(['order_month', 'brand'])['gmv'].sum().unstack().plot()
plt.title('Monthly GMV Year 2019 - Breakdown by Brand',
          loc='center', pad=30, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
# Atur komponen legend menggunakan function plt.legend()
# seperti yang ditunjukkan oleh potongan kode berikut ini:
plt.legend(loc='right', bbox_to_anchor=(1.6, 0.5), shadow=True, ncol=2)
plt.gcf().set_size_inches(12, 5)
plt.tight_layout()
plt.show()
