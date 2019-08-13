import requests
import os

url = 'https://apod.nasa.gov/apod/image/1701/potw1636aN159_HST_2048.jpg'
page = requests.get(url)

f_ext = os.path.splitext(url)[-1]
f_name = 'img{}'.format(f_ext)
with open(f_name, 'wb') as f:
    f.write(page.content)
