#!/speet/Geog250/Labs/8_GeospatialScripting
# preamble

import gdal as gdal
import matplotlib.pyplot as plt

datadir = 'data/'

green1 = gdal.Open('data/LC08_L1TP_042034_20190825_20190903_01_T1_B5.TIF').ReadAsArray()
nir1 = gdal.Open('data/LC08_L1TP_042034_20190825_20190903_01_T1_B6.TIF').ReadAsArray()


green2 = gdal.Open('data/LC08_L1TP_042034_20180806_20180815_01_T1_B5.TIF').ReadAsArray()
nir2 = gdal.Open('data/LC08_L1TP_042034_20180806_20180815_01_T1_B6.TIF').ReadAsArray()


def calc_ndwi(nir,green):
    '''Calculate NDWI from integer arrays'''
    nir = nir.astype('f4')
    green = green.astype('f4')
    ndwi = (green - nir) / (green + nir)
    return ndwi


ndwi2 = calc_ndwi(nir2,green2)
plt.figure(figsize=(12,10))
plt.imshow(ndwi2, cmap='RdYlGn',vmin =-0.6, vmax = 0.5)
plt.colorbar(shrink = 0.7)
plt.title('NDWI August 22 2018')
plt.xlabel('Column #')
plt.ylabel('Row #')

ndwi1 = calc_ndwi(nir1,green1)
plt.figure(figsize=(12,10))
plt.imshow(ndwi1, cmap='RdYlGn', vmin =-0.6, vmax = 0.5)
plt.colorbar(shrink = 0.7)
plt.title('NDWI July 15 2017')
plt.xlabel('Column #')
plt.ylabel('Row #')

plt.figure(figsize = (12,10))
plt.imshow(ndwi2 - ndwi1, cmap='bwr', vmin=-.6, vmax=.5)
plt.colorbar(shrink = 0.7)
plt.title('Difference (2018 - 2017)')
plt.show()
