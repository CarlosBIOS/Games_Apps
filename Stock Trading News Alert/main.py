import requests
from os import getenv
from datetime import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News")
parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': getenv('api_key_alphavantage')
}

request = requests.get('https://www.alphavantage.co/query', params=parameters)
request.raise_for_status()

data_stock: dict = request.json()['Time Series (Daily)']
data_yesterday: str = datetime.now().strftime('%Y-%m-') + f'{int(datetime.now().strftime('%d')) - 1}'
data_2days: str = datetime.now().strftime('%Y-%m-') + f'{int(datetime.now().strftime('%d')) - 2}'
value_yesterday: float = float(data_stock[data_yesterday]['1. open'])
value_2days: float = float(data_stock[data_2days]['1. open'])
percent_change: float = (value_yesterday - value_2days) / value_2days

if abs(percent_change) >= 0.05:
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    parameters = {
        'q': COMPANY_NAME,
        'sortBy': 'publishedAt',
        'from': data_yesterday,
        'to': data_2days,
        'apikey': getenv('api_key_newsapi')
    }

    request = requests.get('https://newsapi.org/v2/everything', params=parameters)
    request.raise_for_status()
    data_news: dict = request.json()['articles'][:3]
    print(data_news)
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    if percent_change > 0.0:
        text = f'Olá Carlos Monteiro👋\n{STOCK}: 🔺{percent_change}%'
    else:
        text = f'Olá Carlos Monteiro👋\n{STOCK}: 🔻{percent_change}%'

    for article in data_news:
        text += f'Headline: {article['title']}\n' + f'Brief: {article['description']}\n'
    client = Client(getenv('account_sid_twilio'), getenv('auth_token_twilio'))
    message = client.messages.create(from_=getenv('phone_number_twilio'), body=text, to=getenv('my_number'))
    print(message.sid)
