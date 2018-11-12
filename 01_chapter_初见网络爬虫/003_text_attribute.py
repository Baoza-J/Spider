from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features = 'html.parser')

nameList = bsObj.findAll(text='the prince')
print(len(nameList))
