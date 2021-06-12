import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
response = requests.get(url)
print(response)
print(response.status_code)
headers = response.headers
print(headers)
body = response.text[:2000]
print(body)

soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.findAll('strong')
print(quotes)

with open('star_wars_html','w') as file:
    for quote in quotes:
        text_only_quote = quote.text
        file.write(text_only_quote + '\n')

with open('star_wars_quotes.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    column_headings = ('QUOTE')
    writer.writerow(column_headings)

    for quote in quotes:
        text_only_quote = quote.text.strip()
        writer.writerow([text_only_quote])
