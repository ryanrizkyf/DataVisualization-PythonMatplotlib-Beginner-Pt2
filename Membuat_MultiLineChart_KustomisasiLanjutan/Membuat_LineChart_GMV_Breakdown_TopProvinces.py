# sudah terlihat cukup jelas jika kenaikan GMW disebabkan oleh provinsi.
# Berhubung kita fokusnya ke provinsi-provinsi yang GMV-nya besar,
# kalau begitu kita highlight untuk top 5 provinsi saja, yang lainnya kita gabungkan menjadi ‘other’

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

# Kemudian, setelah memiliki kolom baru, grafiknya bisa di update.
# Sebagai catatan, untuk mengubah ukuran figure, juga bisa menggunakan
# function plt.gcf().set_size_inches yang diletakkan di akhir code, sebelum plt.show().
# Plot multi-line chartnya
dataset.groupby(['order_month', 'province_top'])[
    'gmv'].sum().unstack(). plot(marker='.', cmap='plasma')
plt.title('Monthly GMV Year 2019-Breakdown by Province',
          loc='center', pad=30, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.legend(loc='upper center', bbox_to_anchor=(1.1, 1), shadow=True, ncol=1)
plt.gcf().set_size_inches(12, 5)
plt.tight_layout()
plt.show()
