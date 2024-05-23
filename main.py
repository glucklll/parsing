from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parsing():
    url = 'https://omgtu.ru/news/?SHOWALL_1=1' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    news = []
    list = []
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    news = soup.findAll('h3', class_='news-card__title') #находим и добавляем заголовки в список news
    for data in news:
        list.append(data.text)
    for data in list:
        print(data)

parsing()
