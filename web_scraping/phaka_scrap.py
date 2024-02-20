import requests 

from bs4 import BeautifulSoup 

from pprint import pprint

url = "https://www.amazon.fr/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser') 

bisben  = soup.find('div', class_= "a-section")
image = bisben.find('img', class_= 'octopus-pc-item-image') 

pprint(image)

# navv = bisben.find('nav').find('div').find('ul')


# Récupératin des images sur le site

# image = soup.find('img', class_= 'mw-file-element')
# img = image.prettify()    
# pprint(img)

# article = [element.text.strip() for element in nav.children if element.name]

# article = []

# for data in navv.children:
#     if data.name:
#         print(data.text.strip())
        
        # article.append()

























