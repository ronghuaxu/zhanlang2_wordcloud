# -*- coding:utf-8 -*-
import requests



# 下载源代码
def download_page(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Cookie':'input your login cookie'
            }
    html=requests.get(url,headers=header).content
    return html

