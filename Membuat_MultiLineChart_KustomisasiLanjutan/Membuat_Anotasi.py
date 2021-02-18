# Anotasi itu mirip seperti teks, hanya saja ada suatu titik tertentu yang
# kita tunjuk untuk diberikan informasi tambahan. Selain itu, kita bisa menambahkan panah melalui anotasi.

# Untuk membuat annotate, gunakan function  plt.annotate.
# Parameter pertama adalah isi teksnya, dan parameter kedua adalah koordinat dari point yang dianotasi.

# Selain itu ada beberapa parameter untuk anotasi yang bisa ditambahkan:
# 1. xytext: Koordinat dari teks. Jika tidak diisi,maka teks akan diletakkan
# di koordinat point yang dianotasi (parameter kedua)
# 2. arrowprops:Konfigurasi dari panah yang ditambahkan di anotasi, berupa dictionary.
# Beberapa hal yang bisa diset:
# arrowstyle: menentukan bentuk dari panah penunjuk. Isinya bisa berupa bentuk seperti
# '->', '-|>', '<->', '-[', dsb. Bisa juga berupa tulisan seperti 'fancy', 'simple', 'wedge', etc.
# connectionstyle: menentukan bentuk dari garis panahnya. Ada beberapa nilai yang bisa digunakan,
# misalnya 'arc' dan 'arc3' yang berupa garis lurus, 'angle' untuk garis berbelok siku,
# 'angle3' untuk garis berbelok lengkung, atau 'bar' untuk berbelok siku dua kali.
# color: menentukan warna dari panah

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

# Mengecek lima provinsi dengan GMV tertinggi
# Buat variabel untuk 5 propinsi dengan GMV tertinggi
top_provinces = (dataset.groupby('province')['gmv']
                        .sum()
                        .reset_index()
                        .sort_values(by='gmv', ascending=False)
                        .head(5))
print(top_provinces)

# Setelah itu, membuat kolom baru, misalnya ‘province_top’.
# Seperti sebelumnya, manfaatkan function apply & lambda.
# Buat satu kolom lagi di dataset dengan nama province_top
dataset['province_top'] = dataset['province'].apply(
    lambda x: x if(x in top_provinces['province'].to_list()) else'other')

# Beriku adalah kode program utuk menganotasi multi-line chart dari 5 provinsi dengan GMV tertinggi
dataset.groupby(['order_month', 'province_top'])[
    'gmv'].sum().unstack().plot(marker='.', cmap='plasma')
plt.title('Monthly GMV Year 2019 - Breakdown by Province',
          loc='center', pad=30, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.legend(loc='upper center', bbox_to_anchor=(1.1, 1), shadow=True, ncol=1)
# Anotasi pertama
plt.annotate('GMV other meningkat pesat', xy=(5, 900000000),
             xytext=(4, 1700000000), weight='bold', color='red',
             arrowprops=dict(arrowstyle='fancy',
                             connectionstyle="arc3",
                             color='red'))
# Anotasi kedua
plt.annotate('DKI Jakarta mendominasi', xy=(3, 3350000000),
             xytext=(0, 3700000000), weight='bold', color='red',
             arrowprops=dict(arrowstyle='->',
                             connectionstyle="angle",
                             color='red'))
plt.gcf().set_size_inches(12, 5)
plt.tight_layout()
plt.show()
