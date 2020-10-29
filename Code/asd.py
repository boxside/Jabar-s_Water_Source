import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

desired_width= 400
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)


air = pd.read_csv(r"C:\Users\fikri\Desktop\pyproj\air.csv")
air_gdf = gpd.read_file(r'C:\Users\fikri\Desktop\pyproj\PROVINSI JAWA_BARAT\PROVINSI_JAWA_BARAT.shp')
air2 = air_gdf[['KABKOTNO', 'KABKOT']]
air4 = pd.DataFrame({ 'kode' :['04','17','16','01','07','03','09','05','12','15','08','10','18','14','13','02','11','06','79'], 'nama_kabupaten_kota' :
                    ['KABUPATEN BANDUNG','KABUPATEN BANDUNG BARAT','KABUPATEN BEKASI','KABUPATEN BOGOR','KABUPATEN CIAMIS','KABUPATEN CIANJUR',
                     'KABUPATEN CIREBON','KABUPATEN GARUT','KABUPATEN INDRAMAYU','KABUPATEN KARAWANG',
                     'KABUPATEN KUNINGAN','KABUPATEN MAJALENGKA','KABUPATEN PANGANDARAN','KABUPATEN PURWAKARTA','KABUPATEN SUBANG','KABUPATEN SUKABUMI',
                     'KABUPATEN SUMEDANG','KABUPATEN TASIKMALAYA','KOTA BANJAR']})

air3= air[air['kondisi'] != 'RUSAK PARAH'].groupby('nama_kabupaten_kota')['jumlah'].sum().reset_index()
air5 = air3.merge(air4, left_on = 'nama_kabupaten_kota', right_on = 'nama_kabupaten_kota')
merged = air_gdf.set_index('KABKOTNO').join(air5.set_index('kode'))
merged['jumlah'].fillna('0', inplace = True)
merged['jumlah']=merged['jumlah'].astype(int)
fig, ax = plt.subplots(1, figsize=(20, 20))

ax.axis('off')
ax.set_title('Persebaran Ketersediaan Sumber Air Desa di Jawa Barat',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged.plot(column='jumlah', cmap='Blues', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)
plt.show()

