# Erros que podem dar na internet:
# 1xx -> Hold On, something it's going to happen
# 2xx -> Here you go, you can enter. For example, 200 que signifa que consegui entrar no site com sucesso
# 3xx -> Go away, you dont have access
# 4xx -> You Screwed Up. For exemple: 404, que significa que o URL já não existe ou 400 que é BAD REQUEST
# 5xx -> I(The Server) Screed Up
# Todos os possiveis errors: https://www.webfx.com/web-development/glossary/http-status-codes/
import requests
from datetime import datetime
from send_emails import send_emails
import time

url = 'http://api.open-notify.org/iss-now.json'
request = requests.get(url)
request.raise_for_status()
data: dict = request.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Os parameters tive que criar para ter acceso aos dados. O url: https://sunrise-sunset.org/api
# O formatted por default está 1, ou seja, criar uma data mais formatada: 5:58:03 AM

MY_LAT, MY_LONG = 41.3696, -8.3078
parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
    'tzid': 'Europe/Lisbon',

}

request = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
request.raise_for_status()
data: dict = request.json()['results']
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if (iss_latitude, iss_longitude) == (MY_LAT, MY_LONG) and (datetime.now().hour >= sunset or datetime.now().hour <=
                                                               sunrise):
        message = 'Subject: Look up\n\n The ISS is above you in the sky!'
        send_emails(message)
