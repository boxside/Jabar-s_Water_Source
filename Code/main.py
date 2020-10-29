#import module
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)

#import dataset
air = pd.read_csv(r"C:\Users\fikri\Desktop\pyproj\air.csv")
air_gdf = gpd.read_file(r'C:\Users\fikri\Desktop\pyproj\PROVINSI JAWA_BARAT\PROVINSI_JAWA_BARAT.shp')

#checking dataset
print(air.head())
#checking if  there are any missing values
print(f'Missing Value:\n',air.isnull().sum())
#delete unnecessary columns
air1= air.drop(['provinsi','kode_kabupaten_kota','satuan'], axis=1)
print(f'columns deleted:\n',air1.head())

#data visualization water pump with condition by regional

plt.rcParams['figure.figsize']=(20, 30)
plt.style.use('dark_background')

sns.catplot(x='nama_kabupaten_kota', y='jumlah', data=air1,palette = 'gnuplot', kind='bar', hue='kondisi', legend=True)
plt.xlabel('Daerah', size=10, labelpad=20)
plt.ylabel('Jumlah(Desa)', size=10, labelpad=20)
plt.title('Jumlah Ketersediaan Sumber Air dan Kondisi Desa di Jawa Barat', fontweight = 30, fontsize = 20)
plt.xticks(rotation = 90, fontsize=12)

#total water source by regional
total_water = air1.groupby('nama_kabupaten_kota')['jumlah'].sum().reset_index().sort_values(by='jumlah', ascending = False)
plt.rcParams['figure.figsize']=(20, 30)
plt.style.use('dark_background')

sns.catplot(x='nama_kabupaten_kota', y='jumlah', data=total_water,palette = 'gnuplot', kind='bar', legend=True)
plt.xlabel('Daerah', size=10, labelpad=20)
plt.ylabel('Jumlah(Desa)', size=10, labelpad=20)
plt.title('Jumlah Ketersediaan Sumber Air Desa di Jawa Barat', fontweight = 30, fontsize = 20)
plt.xticks(rotation = 90, fontsize=12)
plt.show()

#Water source with badly demaged condition
bad_cond = air1[air1['kondisi'] == 'RUSAK PARAH'].groupby('nama_kabupaten_kota')['jumlah'].sum().reset_index().sort_values(by='jumlah', ascending = False)
plt.rcParams['figure.figsize']=(20, 30)
plt.style.use('dark_background')

sns.catplot(x='nama_kabupaten_kota', y='jumlah', data=bad_cond,palette = 'gnuplot', kind='bar', legend=True)
plt.xlabel('Daerah', size=10, labelpad=20)
plt.ylabel('Jumlah(Desa)', size=10, labelpad=20)
plt.title('Jumlah Ketersediaan Sumber Air dengan kondisi Rusak Parah Desa di Jawa Barat', fontweight = 30, fontsize = 20)
plt.xticks(rotation = 90, fontsize=12)
plt.show()