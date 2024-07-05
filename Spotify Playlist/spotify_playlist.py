from bs4 import BeautifulSoup
import requests
from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime


def validate_date(data: str) -> str:
    """Verifica se `str` é um year or not"""
    while True:
        try:
            year, month, day = map(int, data.split('-'))
            if 1900 <= year <= int(datetime.now().strftime('%Y')) and 1 <= month <= 12 and 1 <= day <= 31:
                return data
            else:
                raise ValueError
        except ValueError:
            data = input('Please write a correct date (attention, the year is from 1900): ').strip()


answer: str = validate_date(input('Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ')
                            .strip())

request = requests.get(f'https://www.billboard.com/charts/hot-100/{answer}')
request.raise_for_status()

soup = BeautifulSoup(request.text, 'html.parser')

song_names_spans: list = soup.select("li ul li h3")
song_names: list[str] = [song.getText().strip() for song in song_names_spans]
artist_names_spans: list = soup.select('li ul li span')
artist_names: list = []
for artist in artist_names_spans:
    if len(artist.getText().strip()) >= 3:
        if 'Featuring' in artist.getText().strip():
            artist_names.append(artist.getText().replace(' Featuring ', ',').strip())
        else:
            artist_names.append(artist.getText().strip())

# Para ter acesso ao Dashboard do spotify, fui a este link: https://developer.spotify.com/dashboard

CLIENT_ID: str = getenv('spotify_client_id')
CLIENT_SECRET: str = getenv('spotify_client_secret')
ENDPOINT: str = f'https://api.spotify.com/v1/users/{CLIENT_ID}/playlists'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, show_dialog=True,
                                               cache_path="token.txt", username='Carlos Jjv',
                                               redirect_uri="http://example.com", scope="playlist-modify-private"))

user_id = sp.current_user()["id"]  # Aqui q vai criar o token.txt se colocar o URL no input do run!!!

song_uris: list = []

for index in range(len(song_names)):
    result = sp.search(q=f"track:{song_names[index]} artist:{artist_names[index]}", type="track")
    if result["tracks"]["total"] > 0:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    else:
        print(f"{song_names[index]} doesn't exist in Spotify. Trying to search for similar tracks...")
        result = sp.search(q=f"track:{song_names[index]}", type="track")
        if result["tracks"]["total"] > 0:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        else:
            print(f"{song_names[index]} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{answer} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
