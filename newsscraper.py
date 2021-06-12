import requests
from bs4 import BeautifulSoup

#websites to scrape:
# yahoo, nbc.com, cnn.com, cbs.com, washingtonpost.com
urls = ['https://news.yahoo.com/','https://www.nbcnews.com/','https://www.cnn.com/','https://www.cbsnews.com/','https://www.washingtonpost.com/']
soups=[]
for x in range(0,len(urls)):
    soups.append(BeautifulSoup(requests.get(urls[x]).content, 'html.parser'))
keyword = 'the'

articles = []


for x in range(0,len(soups)):
    articles.append(urls[x])
    for title in soups[x].find_all('a'):
        if keyword.lower() in title.text.lower():        
            articles.append(title.text.strip())

for article in articles:
    print(article)


