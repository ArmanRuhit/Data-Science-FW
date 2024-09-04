import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine

url = 'https://www.sharenews24.com/group/1/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('div', class_='col-md-6 col-sm-12')

data = []
for article in articles:
    title = article.find('h3').text.strip()
    link = article.find('a')['href'].strip()
    description = article.find('p').text.strip() if article.find('p') else "No description"
    date = article.find('span', class_='time').text.strip() if article.find('span', class_='time') else "No date"
    
    data.append([title, date, description, link])

df = pd.DataFrame(data, columns=['Title', 'Date', 'Description', 'Link'])

engine = create_engine('sqlite:///news.db')
df.to_sql('news', engine, index=False, if_exists='replace')

print("Data scraping and storage completed!")
