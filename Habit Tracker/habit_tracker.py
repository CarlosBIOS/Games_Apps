import requests
from os import getenv
import webbrowser
from datetime import datetime

# O link para cada passo: https://pixe.la.

# A função requests.get() é utilizada para recuperar dados de um servidor. Ela envia uma requisição HTTP GET para o URL
# especificado e retorna a resposta do servidor como um objeto Response. O objeto Response contém informações como o
# código de status da resposta, os cabeçalhos e o corpo da resposta.
# A função requests.post() é utilizada para enviar dados para um servidor e criar um novo recurso. Ela envia uma
# requisição HTTP POST para o URL especificado, incluindo os dados a serem enviados no corpo da requisição. A função
# retorna a resposta do servidor como um objeto Response.
# A função requests.put() é utilizada para atualizar um recurso existente num servidor. Ela envia uma requisição HTTP
# PUT para o URL especificado, incluindo os dados atualizados no corpo da requisição. A função retorna a resposta do
# servidor como um objeto Response.
# A função requests.delete() é utilizada para remover um recurso existente num servidor. Ela envia uma requisição HTTP
# DELETE para o URL especificado. A função retorna a resposta do servidor como um objeto Response.

pixela_endpoint: str = 'https://pixe.la/v1/users'
USERNAME: str = getenv('username_pixela')
TOKEN: str = getenv('token_pixela')
GRAPH_ID = 'graph69'
TODAY = datetime.now().strftime('%Y%m%d')

# Relativamente ao post, o token e username, eu próprio criei os valores, diferentemente do get!!!
user_params: dict = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)  {"message":"Success. Let's visit https://pixe.la/@carlosjjv , it is your profile page!"
#                        "isSuccess":true}
# Como já criei a minha conta, agora já posso comment as 2 linhas anteriores!!!

graph_endpoint: str = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config: dict = {
    'id': 'graph69',
    'name': 'Estudo',
    'unit': 'hours',
    'type': 'float',
    'color': 'ajisai',
}

headers: dict = {
    'X-USER-TOKEN': TOKEN,
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)  # {"message":"Success.","isSuccess":true}

addpixel_endpoint: str = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

addpixel_config = {
    'date': TODAY,
    'quantity': '4.30',
}

# response = requests.post(addpixel_endpoint, json=addpixel_config, headers=headers)
# print(response.text)  # {"message":"Success.","isSuccess":true}

updatepixel_endpoint: str = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}'

updatepixel_config = {
    'quantity': '3.30',
}

response = requests.put(updatepixel_endpoint, json=updatepixel_config, headers=headers)
print(response.text)  # {"message":"Success.","isSuccess":true}

# webbrowser.open(f'https://pixe.la/@{USERNAME}')
webbrowser.open(f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html')
