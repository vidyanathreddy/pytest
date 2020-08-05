#! /usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re
from tabulate import tabulate

url = 'https://get.tech/blog/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
soup.prettify()

title_list = []
i = 1
for line in soup.find_all(class_='entry-title'):
    title_list.append([i,line.get_text()])
    i = i+1

print(tabulate(title_list, headers=["S.No", "Title"]))
    


