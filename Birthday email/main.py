from send_emails import send_emails
import pandas
import random
from glob import glob
from datetime import datetime

data: list[dict] = pandas.read_csv('birthdays.csv').to_dict(orient='records')

for index, element in enumerate(data):
    if datetime.now().day == element['day'] and datetime.now().month == element['month']:
        with open(random.choice(glob('letter_templates/*.txt')), encoding='utf-8') as file:
            message: str = file.read()

        messagem: str = f'''\
Subject: Happy Birthday!
{message.replace('[NAME]', data[index]['name'])}
'''
        send_emails(messagem, data[index]['email'])

# Vou a este site para executar todos os dias o código:
# Vou a Files e na pasta que está o documento executo o open bash, dps escrevo python3 main.py
# Tenho que colocar a pass no send_emails, pois se não, não ia dar o código
# Dps, vai a Tasks, coloca a hora e o path: python3 qhome/CarlosMonteiro/Birthday Email/main.py
