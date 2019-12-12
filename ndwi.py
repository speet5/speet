#!/speet/Geog250/Labs/8_GeospatialScripting
# preamble

import pandas as pd
import urllib.request

# download list of L8 scenes from amazon server (20 MB)
print('Downloading complete list of L8 scenes')
s3_scenes = pd.read_csv('http://landsat-pds.s3.amazonaws.com/c1/L8/scene_list.gz', compression='gzip')

#display(scene_urls)

acqDate = pd.to_datetime(s3_scenes['acquisitionDate'])  # create new variable with datetime object
month = acqDate.dt.month        

# use row and path to find latest scene for southern rockies
path = 42
row = 34

# Filter the Landsat Amazon S3 table for images matching path, row, cloudcover and processing state.
scenes = s3_scenes[(s3_scenes.path == path) & (s3_scenes.row == row) & 
                   (s3_scenes.cloudCover <= 5) & 
                   (~s3_scenes.productId.str.contains('_T2')) &
                   (~s3_scenes.productId.str.contains('_RT')) & 
                   ( (month == 8))]#month choice

print(' Found {} images\n'.format(len(scenes)))

# extract scene ids and sort:
scene_urls = sorted(scenes.download_url, reverse=True)

i = 1
url2 = scenes.iloc[i]['download_url']      # the first scene
url2 = url2[0:-10]                          # remove the '/index.html' from the url
scene2 = scenes.iloc[i]['productId']       # extract scene ID
date2 = scenes.iloc[i]['acquisitionDate']  # extract acquisition date

print(url2)
print(scene2)
print(url2+scene2)
print(date2)

i = 0
url1 = scenes.iloc[i]['download_url']      # the first scene
url1 = url1[0:-10]                          # remove the '/index.html' from the url
scene1 = scenes.iloc[i]['productId']       # extract scene ID
date1 = scenes.iloc[i]['acquisitionDate']  # extract acquisition date

print(url1)
print(scene1)
print(url1+scene1)
print(date1)

# combine url + scene + band to specify download path
red_url1 = url1+scene1+'_B{}.TIF'.format(6)
nir_url1 = url1+scene1+'_B{}.TIF'.format(5)

# specify local directory where the data will be downloaded to:
datadir = 'data/'

urllib.request.urlretrieve(red_url1, datadir + scene1 +'_B{}.TIF'.format(6))
urllib.request.urlretrieve(nir_url1, datadir + scene1 +'_B{}.TIF'.format(5))


