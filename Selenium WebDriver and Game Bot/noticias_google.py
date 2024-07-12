import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://www.google.com')

permition_button = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
permition_button.click()

write = driver.find_element(By.NAME, 'q')
write.send_keys('BTS', Keys.ENTER)

noticias = driver.find_element(By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[3]')
noticias.click()

noticia1 = driver.find_element(By.XPATH, '//*[@id="rso"]/div/div/div[2]/div/div/a/div/div[2]/div[2]')
noticia1_text = noticia1.text
print(noticia1_text)
noticia1.click()

button_site = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]')
button_site.click()

paragraphs = driver.find_elements(By.TAG_NAME, 'p')
print(paragraphs)
for paragraph in paragraphs[3:]:
    if len(paragraph.text) != 0 and paragraph.text != 'TODOS OS DIREITOS RESERVADOS':
        with open('noticia', 'a', encoding='utf-8') as file:
            file.write(paragraph.text + '\n')

driver.close()
