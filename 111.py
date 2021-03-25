#from Crypto.Cipher import AES
#import base64
import requests
#import json
#import time

#import random

#import jieba

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'   
}
url='http://www.cuc.edu.cn/'

response = requests.get(url, headers=headers)                  #发送post请求，变量response存储返回的内容
    #response = requests.post(url, headers=headers, data=data, proxies=proxy)  #这个是加了代理的用法
print(response.content)   #这是一个JSON 格式的字符串     

save_path='wangxu.txt'                         #文件保存路径

with open(save_path, 'a', encoding='utf-8') as f:            #学习Python 文件输出的方法，参数'a'的含义？？？再了解下其他的同类型参数的作用
    f.write(str(response.content))