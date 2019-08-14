#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

D = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100\
Safari/537.36',
}
url = 'http://www.bluecore.com.cn/'
headers = D

r = requests.get(url,headers=headers)
r.encoding = r.apparent_encoding
print(r.text)