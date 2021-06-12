import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.indeed.com/jobs?q=computer+science+internships&l=Brooklyn%2C+NY'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
title = []
company = []
dates = []

for header in soup.find_all('h2'):
    title.append(header.text.strip())
for empl in soup.find_all(class_='company'):
    company.append(empl.text.strip())

for date in soup.find_all(class_='date'):
    dates.append(date.text.strip())


for x in range(0, len(title)):    
    print(title[x] + "\n"+ company[x])
    print(dates[x])
    print()


with open('jobs_list.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    column_headings = ('Job Title','Company','Date Posted')
    writer.writerow(column_headings)

    for x in range(0,len(title)):
        row = [title[x],company[x],dates[x]]
        writer.writerow(row)