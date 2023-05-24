# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://sparta:test@cluster0.rgsaqvn.mongodb.net/?retryWrites=true&w=majority')
# db = client.dbsparta

# import requests
# from bs4 import BeautifulSoup

# URL = 'https://music.bugs.co.kr/chart'
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(URL,headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')

# trs = soup.select('#CHARTrealtime > table > tbody > tr')

# for tr in trs:
#     title = tr.select_one('.title').text.strip()
#     rank = tr.select_one('.ranking > strong').text.strip()
#     artist = tr.select_one('.artist > a').text

#     print(rank,title,artist)

#     doc = {
#         'title' : title,
#         'rank' : rank,
#         'artist' : artist
#     }
    
#     db.music.insert_one(doc)