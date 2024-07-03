from bs4 import BeautifulSoup
import requests

URL: str = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
all_movies: list = soup.find_all(name='h3', class_='title')

with open('movies.txt', 'w', encoding='utf-8') as file:
    for movie in reversed(all_movies):
        file.write(movie.getText() + '\n')
