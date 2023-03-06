# import requests
# from bs4 import BeautifulSoup


# def get_html(url):
#     headers = 
#     response = requests.get(url)
#     print(response.status_code)         #get-получать   #response-ответ





# def main():  #функция которая запускает другие функции
#     nootebooks_url = ''  #url- потому что нам нужен адрес
#     pages = '1page='
#     get_html(nootebooks_url)

# main()




#тут  я пыталась парсить сайт work.ua



# import requests
# from bs4 import BeautifulSoup

# URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"
# r = requests.get(URL_TEMPLATE)
# print(r.status_code)
# print(r.text)

# <h2 class="add-bottom-sm"><a href="/ru/jobs/3682040/" title="Комірник, вакансия от 5 ноября 2019">Комірник</a></h2>

# soup = abs(r.text,"html.parser") #TypeError: bad operand type for abs(): 'str'
#а до этого там был один элемент (r.text, "html.parser") и было ощибка  TypeError: abs() takes exactly one argument (2 given)
# vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
# for name in vacancies_names:
#     print(name.a['title'])


# vacancies_info = soup.find_all('p', class_='overflow')
# for name in vacancies_names:
#     print('https://www.work.ua'+name.a['href'])
# for info in vacancies_info:
#     print(info.text)

# if start == "2":
#     with open("highscore.txt", "a+") as hisc:
#         hisc.write("{}\n".format(count))



#вторая попытка:


import requests
from bs4 import BeautifulSoup as bs    #импортировала всю эту хуйню
# import pandas as pd
#pandas — это библиотека анализа данных с открытым исходным кодом, 
#построенная на основе языка программирования Python.


# URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"
# r = requests.get(URL_TEMPLATE)
# print(r.status_code)         #потом я сделала гед запрос (200)Статус 200 состояния HTTP — означает,
# # что мы получили положительный ответ от сервера.
# print(r.text)     #получила в виде текста очень много всего

# soup = bs(r.text, "html.parser")
# vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
# for name in vacancies_names:
#     print(name.a['title'])     #тоже получила много всего,я думаю это ваканции


# #теперь я пробую спарсить каждую ссылку на ваканцию:

# vacancies_info = soup.find_all('p', class_='overflow')
# for name in vacancies_names:
#     print('https://www.work.ua'+name.a['href'])
# for info in vacancies_info:
#     print(info.text)


# Полная занятость. Опыт работы от 2 лет. Высшее образование.
#                             Меблевій компанії «Максимум-Плюс» потрібен менеджер з продажу Вимоги:    досвід роботи у сфері продажу…⁠


#             Полная занятость. Опыт работы от 1 года.
#                             Ми, міжнародна ІТ компанія Headway.Global! У зв’язку з активним і стабільним зростанням, шукаємо відповідального,…⁠


#             Полная занятость, неполная занятость. Также готовы взять студента, человека с инвалидностью.
#                             Розпочни свій кар'єрний шлях разом із нами :) МакДональдз — це міжнародна компанія, що надасть тобі унікальні…⁠


#             Полная занятость. Опыт работы от 1 года. Среднее специальное образование.
#                             В дистрибюторскую компанию «МО ЛК ОМ» г. Одесса, которая занимается молочной продукцией торговой марки…⁠


#             Полная занятость. Опыт работы от 1 года. Высшее образование.
#                             Приглашаем на постоянную работу ориентированного на результат технически грамотного менеджера, который…⁠ 


import requests
from bs4 import BeautifulSoup as bs
import csv
# import pandas as pd

URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"
FILE_NAME = "test.csv"


def write_to_csv(result_list):
    with open('my_file.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(result_list)


def parse(url = URL_TEMPLATE):
    result_list = {'href': [], 'title': [], 'about': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
    vacancies_info = soup.find_all('p', class_='overflow')
    for name in vacancies_names:
        result_list['href'].append('https://www.work.ua'+name.a['href'])
        result_list['title'].append(name.a['title'])
    for info in vacancies_info:
        result_list['about'].append(info.text)
    # print(list(map(len, result_list.values())))
    print(result_list)
    # write_to_csv(result_list)
    return result_list

parse(URL_TEMPLATE)

# df = pd.DataFrame(data=parse())
# df.to_csv(FILE_NAME)
#ModuleNotFoundError: No module named 'pandas' короче как я поняла мне нужно скачать панду для результата
#NameError: name 'pd' is not defined. Did you mean: 'id'?  а если без этой панды выходит такая ошибка



#я нашла как скачать панду но вопрос можно ли его использовать внутри верту-го каб?
#pip3 install --upgrade 
#пробовала как conda install и пробовала pip install
#pandas для создания фрейма данных и lxml, чтобы изменить HTML на формат, удобный для Python.


#короче способ без использование pandas 




import re
from bs4 import BeautifulSoup

with open("blank/index.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# .find() .find_all()
# page_h1 = soup.find("h1")
# print(page_h1)
#
# page_all_h1 = soup.find_all("h1")
# print(page_all_h1)
#
# for item in page_all_h1:
#     print(item.text)

# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

# user_name = soup.find(class_="user__name").find("span").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span").text
# print(user_name)

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)

# for item in find_all_spans_in_user_info:
#     print(item.text)

# print(find_all_spans_in_user_info[0])
# print(find_all_spans_in_user_info[2].text)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_links)

# all_a = soup.find_all("a")
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")

# .find_parent() .find_parents()

# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# post_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_div)

# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
# print(post_divs)

# .next_element .previous_element
# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)
#
# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)

# .find_next_sibling() .find_previous_sibling()
# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)

# prev_sib = soup.find(class_="post__date").find_previous_sibling()
# print(prev_sib)

# post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text
# print(post_title)

links = soup.find(class_="some__links").find_all("a")
# print(links)
#
# for link in links:
#     link_href_attr = link.get("href")
#     link_href_attr1 = link["href"]
#
#     link_data_attr = link.get("data-attr")
#     link_data_attr1 = link["data-attr"]
#
#     print(link_href_attr1)
#     print(link_data_attr1)

# find_a_by_text = soup.find("a", text="Одежда")
# print(find_a_by_text)
#
# find_a_by_text = soup.find("a", text="Одежда для взрослых")
# print(find_a_by_text)

# find_a_by_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text)

find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
print(find_all_clothes)