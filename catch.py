# -*- coding: utf-8 -*-

from Crypto.Cipher import AES #网页
import base64#网页
import requests#网页

import time
import random

import json 

from wordclound_show import *         #这个是我自定义的头文件

#访问标头
headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'Host':'music.163.com',
    'Origin':'https://music.163.com',
    'Referer':'https://music.163.com/song?id=1297747234',#该地址为歌曲的页面网址
    'User-Agent':'xxxxxxxxxxxxxxxxxxx'   
}

#proxy = {'http':'175.42.158.68:9999'}   #加个代理，网易就不会干掉我的IP，但是.....目前这个代理不能用

#以下四个参数为固定的加密参数
#first_param = xxxxxxxxxxx         #定义在get_params()函数里了，为局部变量，只能在函数范围内使用
second_param = "010001"            #全局变量，代码里哪里都能直接用
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud" 

#爬虫框架
#网页请求返回
#页面代码


#获取参数
#    page: 爬取的页码 
def get_params(page):  
    iv = b"0102030405060708"   #密钥         #引申学习 ——> python字符串前缀u，b，r，f用法
    first_key = forth_param
    second_key = 16 * 'F'
    if(page == 1): # 如果为第一页
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'   
                                                    #offset就是（评论页数-1） * 20，total在第一页是true，其余是false
        h_encText = AES_encrypt(first_param, first_key, iv)
    else:
        offset = str((page-1)*20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' %(offset,'false')  
                                                     #学习Python格式化拼接的方法，%(offset,'false')
        h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)#调用AES分组加密算法函数，获得加密后的内容   AES  RSA  哈希函数。 国密算法 SM4  SM2  SM3   
    return h_encText
###########################################################################


#获取密钥
def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey
    
#AES分组加密算法函数
#    text: 要加密的内容
#    key:  密钥
#    iv:   密钥向量
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16          #len()函数的作用：？
    text = text + pad * chr(pad)       #chr()函数的作用：？
    text=text.encode("utf-8")            #类型转换：str to bytes 
    encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)  
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text) 
    return encrypt_text.decode('utf-8')  #类型转换：bytes to str
                                         # bytes（一堆二进制的数字，如：b'11001010'）主要是给在计算机看的，string主要是给人看的

#访问网易云服务器, 获取评论内容
#    url:       网址
#    params:    参数
#    encSecKey: 密钥
def get_json(url, params, encSecKey):
    data = {
         "params": params,# 密文：由页码加密后生成；
         "encSecKey": encSecKey
    }    
    
    response = requests.post(url, headers=headers, data=data)                  #发送post请求，变量response存储返回的内容
    #response = requests.post(url, headers=headers, data=data, proxies=proxy)  #这个是加了代理的用法
    print(response.status_code)
    return response.content  #这是一个JSON 格式的字符串

#抓取评论
#    url:  网址
#    page_o: 要爬取的首页
#    page_d：要爬取的末页

def get_all_comments(url,page_o,page_d):
    all_comments_list = [] # 存放所有评论
    for i in range(page_o,page_d):  # 逐页抓取

        params = get_params(i)#变动的  
        encSecKey = get_encSecKey()#固定的

        json_text = get_json(url,params,encSecKey) ########

        json_dict = json.loads(json_text) #JSON格式的字符串处理办法      
        try:   
            #for item in json_dict['hotComments']:    #热评的数量比较少
            for item in json_dict['comments']:
                try:
                    comment = item['content']               #评论内容
             
                    comment_info = str(comment)              #str()函数的作用：？
                    all_comments_list.append(comment_info)   #list.append() 给 列表型变量追加 内容
                except:
                    print(comment)             
        except:
            print('\n')                             #try：  except: 的用法？
        
        print('第%d页抓取完毕!' %(i))                      #格式化屏幕打印的写法 print('  %变量类型简写  ' %(变量名))
        
        #sleep_time=random.choice(range(6,15))            #从6到15之间取个随机数，作为休眠时间
        sleep_time=random.randrange(6,15)

        print(f"休眠:{sleep_time}s") 
        #print('休眠:%d s'%(sleep_time))                  #复习 python字符串前缀u，b，r，f用法
                                                          # python的单引号 '' 和双引号 ""  没区别,可以混用  
        time.sleep(sleep_time)                            #设置休眠时间，跑慢点，减轻服务器负担，避免触发反爬机制
    return all_comments_list

#主函数  main  
if __name__ == "__main__":
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_1297747234/?csrf_token="   #  R_SO_4_xxxxxxx加上歌曲的id就是抓取评论的API接口
    
    all_comments = get_all_comments(url, page_o=1,page_d=3)          # 需要爬取的页面范围    
    
    print(all_comments)                                              #打印爬到的内容


    file_tag=time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())    #将当前时间作为输出文本文件名
    #file_tag='All Night Long'                                        #将歌曲名为输出文本文件名

    save_path=f'all_comments_{file_tag}.txt'                         #文件保存路径

    for line in all_comments: #遍历
        with open(save_path, 'a', encoding='utf-8') as f:            #学习Python 文件输出的方法，参数'a'的含义？？？再了解下其他的同类型参数的作用 x +x w b
            f.write(line+'\n')                                       #学习转义字符。 '\n' 作用为换行
   
