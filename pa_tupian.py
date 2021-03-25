#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 17:54
# 爬取图片

import requests
import random
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
# 这里我使用了代理  你可以去掉这个代理IP 我是为了后面大规模爬取做准备的
proxies = {
    'https': '218.75.69.50:39590'
}




# 解析网页 获取图片
def parse(img_url):

        # 获得每张图片的二进制内容
    img = requests.get(img_url, headers=headers, proxies=proxies).content
        # 定义要存储图片的路劲
    path = str(x) + ".jpg"
        # 将图片写入指定的目录 写入文件用"wb"
    with open(path, 'wb') as f:
        f.write(img)
        time.sleep(random.randrange(6,15))
        print("正在下载第{}张图片".format(x))
        x += 1
    print("写入完成")


def main():
    url = "https://cags.ltfc.net/cagstore/57ceec056d5f4b68798e4913/18/16_4.jpg"
    parse(url)


if __name__ == "__main__":
    main()
