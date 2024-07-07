# O módulo BeautifulSoup do Python é utilizado para a extração de dados de arquivos HTML e XML. Ele cria uma árvore de
# análise a partir dos conteúdos de uma página web, permitindo a navegação, pesquisa e modificação desses dados de
# maneira simples e eficiente.
# Tem limitações, por exemplo, não pode usar em todos os browsers. Por isso, no futuro vamos usar o Selenium Webdriver
from bs4 import BeautifulSoup
import requests
# import lxml
# O módulo lxml do Python é uma biblioteca amplamente usada para trabalhar com XML e HTML de forma eficiente e rápida.

with open('website.html', encoding='utf-8') as file:
    content: str = file.read()

print(content, '\n')

# soup = BeautifulSoup(content, 'lxml')
# Se o html não der, uso o código de cima
soup = BeautifulSoup(content, 'html.parser')

print(soup.title)  # <title>Angela's Personal Site</title>
print(soup.title.name)  # title
print(soup.title.string)  # Angela's Personal Site
# print(soup.prettify())
print(soup.a)  # <a href="https://www.appbrewery.co/">The App Brewery</a>
print(soup.p)  # <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
print(soup.li)  # <li>The Complete iOS App Development Bootcamp</li>

print('*' * 80)

print(soup.find_all(name='a'))
# [<a href="https://www.appbrewery.co/">The App Brewery</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">My
# Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]
print(soup.find_all(name='h1'))  # [<h1 id="name">Angela Yu</h1>]
print(soup.find_all(name='li'))
# [<li>The Complete iOS App Development Bootcamp</li>, <li>The Complete Web Development Bootcamp</li>, <li>100 Days of
# Code - The Complete Python Bootcamp</li>]

all_a_tags = soup.find_all(name='a')
for a_tag in all_a_tags:
    print(a_tag.getText())
    print(a_tag.get('href'))

heading = soup.find(name='h1', id='name')
print('\n', heading.string)  # Angela Yu

section_heading = soup.find(name='h3', class_='heading')
print(section_heading)  # <h3 class="heading">Books and Teaching</h3>
print(section_heading.string)  # Books and Teaching
print(section_heading.get('class'))  # ['heading']

print('*' * 80)

company_url = soup.select_one(selector='p a')
print(company_url)  # <a href="https://www.appbrewery.co/">The App Brewery</a>
print(company_url.get('href'))  # https://www.appbrewery.co/

print('-' * 80)

name = soup.select_one(selector='#name')
print(name)  # <h1 id="name">Angela Yu</h1>
print(name.string)  # Angela Yu

print('-' * 80)

h3 = soup.select_one(selector='.heading')
print(h3)  # <h3 class="heading">Books and Teaching</h3>
print(h3.string)  # Books and Teaching

print('*-' * 80)

# Este url é mais difícil, porque o site não é static: https://news.ycombinator.com/news
# TODO: SE ESCREVER robots.txt DPS DO LINK, SEI O QUE POSSO E O Q NÃO POSSO FAZER NO SITE COM UM BOT!!!!!
#   https://news.ycombinator.com/robots.txt
request = requests.get('https://appbrewery.github.io/news.ycombinator.com/')
request.raise_for_status()
content: str = request.text

soup = BeautifulSoup(content, 'html.parser')
print(soup.prettify())
all_title_tags: list = soup.find_all(name='a', class_='storylink')
print(len(all_title_tags))  # 30
all_score: list = soup.find_all(name='span', class_='score')

dictionary: dict = {}
num = 0
for tag in all_title_tags:
    dictionary[int(all_score[num].string.split()[0])] = (tag.get('href'), tag.getText())
    num += 1

print(dictionary[max(dictionary)][1])  # Mozilla lays off 250 employees while it refocuses on commercial products
