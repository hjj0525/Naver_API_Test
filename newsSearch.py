import csv
import os
import sys
import requests 
import time
client_id = "-----api id-----"
client_secret = "----api secret----"

keyword = input("검색하고 싶은 뉴스를 입력하세요: ") 
url = "https://openapi.naver.com/v1/search/news.json"
headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}

display_cnt = 100

for x in range(10):
    params = {'query':keyword, 'display':100, 'sort':'sim', 'start':x*display_cnt+1}
    result = requests.get(url, headers = headers, params=params).json()
    time.sleep(1)
    for i, item in enumerate(result['items']):
        print(i+1+x*display_cnt, " 번째")
        print(item['title'].replace('<b>','').replace('</b>',''))
        print(item['pubDate'][:-5])
        print(item['link'])

        

