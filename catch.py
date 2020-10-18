# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import requests
import json
import time

import random
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt
import codecs
import jieba


headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'Host':'music.163.com',
    'Origin':'https://music.163.com',
    'Referer':'https://music.163.com/song?id=1297747234',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38'   
}

#first_param = '{rid:"", offset:"20", total:"false", limit:"50", csrf_token:""}'
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
       
        try:   
            for item in json_dict['comments']:
                comment = item['content'] # 评论内容
                comment_info = str(comment)
                all_comments_list.append(comment_info)
        except:
            print(json_dict)
        print('第%d页抓取完毕!' % (i+1))
        sleep_time=random.choice(range(6,15))
        print(f"休眠：{sleep_time}s")
        time.sleep(sleep_time)  #爬取过快的话，设置休眠时间，跑慢点，减轻服务器负担
    return all_comments_list



    #生成词云
def wordcloud(all_comments):
    # 对句子进行分词，加载停用词
    # 打开和保存文件时记得加encoding='utf-8'编码，不然会报错。
    def seg_sentence(sentence):
        sentence_seged = jieba.cut(sentence.strip(), cut_all=False)  # 精确模式
        stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]  # 这里加载停用词的路径
        outstr = ''
        for word in sentence_seged:
            if word not in stopwords:
                if word != 't':
                    outstr += word
                    outstr += " "
        return outstr
    for line in all_comments:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        with open('outputs.txt', 'a', encoding='utf-8') as f:
            f.write(line_seg + 'n')

    data = open('outputs.txt', 'r', encoding='utf-8').read()
    my_wordcloud = WordCloud(
        scale=2,
        background_color='white',  #设置背景颜色
        max_words=200,  #设置最大实现的字数
        max_font_size=50,
        font_path=r'simhei.ttf',  #设置字体格式，如不设置显示不了中文
    ).generate(data)

    plt.figure()
    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.show()  # 展示词云



if __name__ == "__main__":
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_1297747234/?csrf_token="   #  R_SO_4_加上歌曲的id就是抓取评论的API
    
    all_comments = get_all_comments(url, page=10)  # 需要爬取的页面数    
    #all_comments=['意思就是如果状元郎如果娶了她的话，皇上就会诛他九族.', '阿淦a', '桃李春风，浊酒与誰共饮？', '所以就是爱男生没有一个好东西', '这有什么的', '敢不敢玩把大的，把自己喜欢的人的名字打出来，直接打全名[大笑]', '历史不会改变', '对不起，我当时心情太不好了，语言可能过于激烈了，我当时喜欢的人喜欢的同桌也喜欢别人了，可能看到这种讨论爱情的的评论可能就有点不高兴……对不起我会删除评论的', '收到', '酒入豪肠，七分酿成了月光，余下的三分，啸成了剑气。绣口一吐，就是半个盛唐。', '叶长安，有吗？', '[多多大哭]', '抖音又毁了一首歌', '谪仙人', '高手过招', '加油', '有趣的灵魂啊', '所以是什么意思', '我是不听古风的，只因这首是李白[大笑]', '为什么我想到了探子打算报告禁急坏状况，将军无奈的张开双臂迎接死……', '平陆成江？', '郭子仪我家的祖先，家里老人给我讲过', '我还记得叶里，唱东宫《初见》，把我听哭的', '为啥说的跟杜甫他老人家引发的乱世一样', '世上谪仙——姚温玉\n红尘浪客——乔天涯', '同城', '有李白的浪劲儿了', '目前大体三种说法，不止醉酒捞月这一个', '发现评论区个个都是文豪大佬', '你可曾执笔写春秋？', '盗no', '相传死于醉酒捞月，可是世人又说李白千杯不醉 ，呵', '我们班要整体换座位 希望我的同桌学习好一点可爱一点吧啊啊啊啊啊', '这个歌太火了', '八表同昏', '所以要跟懂的人讲，懂自然懂。不懂装懂就是恶臭，人生懂你的就几个就好了，朋友太多消耗自己的时间，不过正常社交该有还是有', '哎呀！你给我点过赞诶', '就算没有拯救世界又怎么样。我爸爸依然是我心中的英雄', '毕业的前一天，他看着同桌的她戴着耳机写着卷子，很想对她表白却不好意思开口，终于，他试探着叫了她的名字，她一点反应也没有，依然写着卷子，于是他很小声的把想对她说的话全部说出；打铃下课了，他离开了座位，同桌的她松开暂停键泪流满面。']
    
    print(all_comments)

    #词云打印
    #wordcloud(all_comments)

    file_tag=time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    #file_tag='歌名'

    save_path=f'all_comments_{file_tag}.txt'

    for line in all_comments:
        with open(save_path, 'a', encoding='utf-8') as f:
            f.write(line+'\n')
        
   
