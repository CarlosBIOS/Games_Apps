# O Selenium Python é uma biblioteca de código aberto que permite automatizar a interação com navegadores web a partir
# da linguagem de programação Python. Ele fornece um conjunto de ferramentas para controlar navegadores como Firefox,
# Chrome, Edge e Safari, permitindo que você execute diversas ações como:

# Abrir e navegar em páginas da web: Você pode programar o Selenium para acessar URLs específicas, carregar páginas e
# navegar entre elas.
# Preencher formulários e campos de texto: Automatize a digitação de dados em formulários web, campos de login, caixas
# de pesquisa e outros elementos interativos.
# Clicar em botões e links: Simule cliques em botões, links e outros elementos clicáveis para interagir com a página.
# Localizar e manipular elementos HTML: Utilize métodos para encontrar elementos específicos na página HTML, como por
# ID, classe, nome ou seletor CSS.
# Executar JavaScript: Execute scripts JavaScript no contexto da página web para realizar ações mais complexas.
# Capturar screenshots e gravar vídeos: Capture imagens da tela ou grave vídeos da navegação para documentar os testes
# ou demonstrar o funcionamento de um site.
# Fazer scrap de dados: Extraia dados de páginas web, como preços de produtos, informações de contato ou conteúdo de
# artigos.
# https://selenium-python.readthedocs.io
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome Browser Open after program finishes:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1')
driver.get('https://www.python.org/')

# prize_dollar = driver.find_element(By.CLASS_NAME, 'a-price-whole')
# prize_cents = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
#
# print(prize_dollar.text, prize_cents.text, sep='.')  # 99.99

search = driver.find_element(By.NAME, 'q')
print(search.tag_name)  # input
print(search.get_attribute('placeholder'))  # Search

button = driver.find_element(By.ID, 'submit')
print(button.size)

# Dentro do inspecionar elementos, vais ao copy e dps copy selector
# P1: CSS Selector
url = driver.find_element(By.CSS_SELECTOR, '#content > div > section > div.list-widgets.row > div.medium-widget.'
                                           'event-widget.last > div > ul > li:nth-child(1) > a')
print(url.text)  # Django - The Powerhouse

# P2: Xpath Selector
# Dentro do inspecionar elementos, vais ao copy e dps copy Xpath
# https://www.w3schools.com/xml/xpath_intro.asp
url = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/a')
print(url.text)  # Django - The Powerhouse

print('*' * 80)

menu = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
menu_items: list = [item.text for item in menu][0].split('\n')
print(menu_items)
dicti = {}
value = 0
for index in range(0, 10, 2):
    dicti[value] = {'time': menu_items[index], 'name': menu_items[index + 1]}
    value += 1

print(dicti)
