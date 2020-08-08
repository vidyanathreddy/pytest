#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup


url = 'https://www.lipsum.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
soup.prettify()

title_list = []
i = 1

for line in soup.find_all('h3'):
    title_list.append([i,line.get_text()])
    i = i+1
txt2 = ""

for tabrow in title_list:
    r1 = "<tr><td>" + str(tabrow[0]) + "</td>"
    r2 = "<td>" + tabrow[1] + "</td></tr>"
    txt2 = txt2 + r1 +r2

txt2 = txt2 + "</table>"


txt1 = "<table> <tr><th>S.No</th><th>Article Title</th></tr>"

f = open('/var/www/html/index.html','w')
f.write(txt1+txt2)
f.close()


