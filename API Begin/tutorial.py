# Erros que podem dar na internet:
# 1xx -> Hold On, something it's going to happen
# 2xx -> Here you go, you can enter. For example, 200 que signifa que consegui entrar no site com sucesso
# 3xx -> Go away, you dont have access
# 4xx -> You Screwed Up. For exemple: 404, que significa que o URL já não existe
# 5xx -> I(The Server) Screed Up
# Todos os possiveis errors: https://www.webfx.com/web-development/glossary/http-status-codes/
import requests

url = 'http://api.open-notify.org/iss-now.json'
request = requests.get(url)

if request.status_code == 200:
    print(request.json())
else:
    print(f'Deu um erro: {request.status_code}')
