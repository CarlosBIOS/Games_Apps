import requests
from bs4 import BeautifulSoup
from send_emails import send_emails
from twilio.rest import Client
import os


URL_ENDPOINT: str = ('https://www.amazon.com/Animal-Crossing-New-Horizons-Nintendo-Switch/dp/B07SL6ZXBL/ref=sr_1_1?crid'
                     '=25EK698FB592H&dib=eyJ2IjoiMSJ9.Z0M_HNQrO_AR7cweCXN2UEK4KRiVLW1TkbL2kxOSTCb8lqOcFIPzLad5sw8mOEA3H'
                     'LTkU7cPaYTeqMDlfXGI-kznl4hEKNbUlcECCEVk8ew0Y6nwhdaNDqUgQl4B0M2isn51vLA9yTI434P6qo5EFu56ouCLPCoIxl'
                     'B69dZfP519nWlMM3lRzSu8XgOrKUC6ReNFi2UsWQ83_j5xhWl1hmuIfAm8yP16jnfwtAth9ro.7PnFcuEYITKri25hCNO23EY'
                     'qU0gk-6HmZhMXNZnmed4&dib_tag=se&keywords=animal%2Bcrossing&qid=1720264070&sprefix=animal%2B%2Caps'
                     '%2C254&sr=8-1&th=1')

HEADERS: dict = {
    "User-Agent": "Chrome/84.0.4147.125",
    "Accept-Language": "pt-PT"
}

request = requests.get(URL_ENDPOINT, headers=HEADERS)
request.raise_for_status()

soup = BeautifulSoup(request.text, 'lxml')
print(soup)

price_number: float = float(soup.select_one('div span .a-price-whole').getText() +
                            soup.select_one('div span .a-price-fraction').getText())
print(price_number)
if price_number <= 48.0:
    message: str = f'Atenção, o preço do cross animal está {price_number}. Run to buy neste link:\n {URL_ENDPOINT}'
    mesage = f'''
Subject: The animal Crossing está mais barato!

O preço do cross animal está {price_number}. Run para comprar neste link:\n{URL_ENDPOINT}
'''
    send_emails(mesage)
    client = Client(os.getenv('account_sid_twilio'), os.getenv('auth_token_twilio'))
    client.messages.create(from_=os.getenv('phone_number_twilio'), body=message, to=os.getenv('my_number'))
