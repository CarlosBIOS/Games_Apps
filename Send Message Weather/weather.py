import requests
import os
from twilio.rest import Client

# parametrs = {
#     'lat': 41.3696,
#     'lon': -8.3077,
#     'appid': os.getenv('api_key_openweather'),
# }
#
# request = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parametrs)
# request.raise_for_status()
# print(request.json())

parametrs = {
    'lat': 41.36956373522274,
    'lon': -8.307656282406374,
    'appid': os.getenv('api_key_openweather'),
    'cnt': 4,
    'units': 'metric',
    'lang': 'pt'
}

request2 = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parametrs)
request2.raise_for_status()

data: dict = request2.json()['list']

text: str = ''

for index in range(len(data)):
    text += (f'Às {data[index]['dt_txt'][11:16]} vai estar {data[index]['weather'][0]['main']}, ou seja,'
             f' {data[index]['weather'][0]['description']}. A temperatura mínima é {data[index]['main']['temp_min']}ºC'
             f' e a temperatura máxima é {data[index]['main']['temp_max']}ºC.\n')

client = Client(os.getenv('account_sid_twilio'), os.getenv('auth_token_twilio'))
message = client.messages.create(from_=os.getenv('phone_number_twilio'), body=text, to=os.getenv('my_number'))
print(message.sid)
