import requests
headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/69.0.3497.100 Safari/537.36'
        }
url = "https://music.163.com/playlist?id=2722916074"
r = requests.get(url=url,headers=headers)
print(r.text)