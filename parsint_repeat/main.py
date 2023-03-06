import json

import requests

from bs4 import BeautifulSoup as BS

# BASE_URL ='https://www.labirint.ru/'
# def get_soup(url:str) -> BS:
#     response = requests.get(url)
#     soup = BS(response.text, 'lxml')


import requests, json

image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLSM7UagZal_KSGQeZ1QgK0hScu7dtjnO2Ew&usqp=CAU'

response = requests.get(image_url)

with open("test.jpg", "wb") as file:
    file.write(response.content)