# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import requests
import json
import time
import random




headers = {
    'Cookie': 'appver=1.5.0.7573471;',
    'Host':'music.163.com',
    'Origin':'https://music.163.com',
    'Referer':'https://music.163.com/song?id=374597',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

first_param = '{rid:"", offset:"20", total:"false", limit:"50", csrf_token:""}'
#offset就是（评论页数-1） * 20，total在第一页是true，其余是false

second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"

# 获取参数
def get_params(page): # page为传入页数
    iv = b"0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    if(page == 1): # 如果为第一页
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
        h_encText = AES_encrypt(first_param, first_key, iv)
    else:
        offset = str((page-1)*20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' %(offset,'false')
        h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey
    

def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    text=text.encode("utf-8")
    encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text.decode('utf-8')


def get_json(url, params, encSecKey):
    data = {
         "params": params,
         "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content

# 抓取某一首歌的前100页评论
def get_all_comments(url,page):
    all_comments_list = [] # 存放所有评论
    for i in range(page):  # 逐页抓取
        params = get_params(i+1)
        encSecKey = get_encSecKey()
        json_text = get_json(url,params,encSecKey)
        json_dict = json.loads(json_text)
        print(json_dict)
        try:   
            for item in json_dict['comments']:
                comment = item['content'] # 评论内容
                comment_info = str(comment)
                print(comment)
                all_comments_list.append(comment_info)
        except:
            print(json_dict)
        print('第%d页抓取完毕!' % (i+1))
        time.sleep(random.choice(range(2,6)))  #爬取过快的话，设置休眠时间，跑慢点，减轻服务器负担
    return all_comments_list


if __name__ == "__main__":
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_374568/?csrf_token="   #  R_SO_4_加上歌曲的id就是抓取评论的API
    
    all_comments = get_all_comments(url, page=5)  # 需要爬取的页面数
    print(all_comments)
        
   
