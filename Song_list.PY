'''
# -*- coding: utf-8 -*-
from urllib import request
import re

url = 'https://music.163.com/#/playlist?id=317113395'
html = request.urlopen(url).read().decode('utf-8')
pa = re.compile("<a\shref=..song.id=\d{1,20}..>.+?<.a>")//使用正则表达式提取
dataList = pa.findall(html)

num = 1
for data in dataList:
	print(str(num) + "   " +data)
	num += 1
'''

import requests
headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/69.0.3497.100 Safari/537.36'
        }
url = "https://music.163.com/playlist?id=2722916074"
r = requests.get(url=url,headers=headers)
print(r)

with open('song_list.txt', 'a', encoding='utf-8') as f:      
    f.write(r.text)   