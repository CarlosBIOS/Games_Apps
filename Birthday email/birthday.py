from send_emails import send_emails
from datetime import datetime
import random

if datetime.now().weekday() == 0:
    with open('quotes.txt', encoding='utf-8') as file:
        data: list = []
        for element in file:
            data.append(element.strip())

    message = f'''\
Subject: Monday Motivation
{random.choice(data)}
'''
    send_emails(message)


