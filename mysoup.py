# require to import from PyCharm the BeautifulSoup4
from bs4 import BeautifulSoup

import requests

url = "http://www.study-io.com/java/89/";

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data,  "html.parser" )

for link in soup.find_all('a'):
    print(link.get('href'))
