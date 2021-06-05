import os
import sys
import requests 
client_id = "-----api id-----"
client_secret = "----api secret----"

x = 0
userInput = '1'
keyword = input("블로그 검색: ")
while(userInput=='1'):
    url = "https://openapi.naver.com/v1/search/blog?query="+ keyword + '&display=10'
    headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}
    params = {'keyword':keyword, 'display':10, 'start':1+x*10}
    result = requests.get(url, headers = headers, params=params).json()

    for item in result['items']:
        print(item['title'].replace('<b>','').replace('</b>',''))
        print(item['description'].replace('<b>','').replace('</b>',''))
        print(item['link'])

    x+=10
    
    userInput = input("다음 페이지는 1, 끝내시려면 0 ")
    

