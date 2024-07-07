from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

url_wiki: str = 'https://en.wikipedia.org/wiki/Main_Page'
driver.get(url_wiki)

number_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(number_articles.text)

# Clica e se tiver um a(anchor), vai clicar no URL!!
# number_articles.click()

# Find Element by Link Text:
all_portals = driver.find_element(By.LINK_TEXT, 'Content portals')  # O text que show no site que pode ser clicado
# all_portals.click()

# Write no input:
search = driver.find_element(By.NAME, 'search')
search.send_keys("Python", Keys.ENTER)

# driver.close()  # fecha um seperador em específico
# driver.quit()  # fechas todos seperadores
