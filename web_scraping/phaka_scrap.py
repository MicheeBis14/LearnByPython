import json
import requests 
from bs4 import BeautifulSoup 
from pprint import pprint


url = "https://www.docstring.fr/api/books_to_scrape/index.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser') 
categories = soup.find('div', class_='side_categories')

cat_data = categories.find('ul').find('li').find('ul')

for cat in cat_data.children:
        if cat.name:
                print(cat.text.strip())


# 






















