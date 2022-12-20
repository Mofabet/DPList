#!/usr/bin/env python
from fileinput import close
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

with open('list.txt') as file:
  urls = file.read().splitlines()

names = []
avrg_prices = []
low_prices = []
high_prices = []

for url in urls:
    page = requests.get(url)
    soup = bs(page.content)
    names.extend([i.text for i in soup.find_all(class_="product-title")])
    avrg_prices.extend([i.text for i in soup.find_all(class_='blue-big')])
    low_prices.extend([i.text for i in soup.find_all(itemprop="lowPrice")])
    high_prices.extend([i.text for i in soup.find_all(itemprop="highPrice")])

df = pd.DataFrame({'Name': names,
                   'Average prices': avrg_prices,
                   'Minimum prices': low_prices,
                   'Maximum prices': high_prices,})
df.to_excel('./pricelist.xlsx')