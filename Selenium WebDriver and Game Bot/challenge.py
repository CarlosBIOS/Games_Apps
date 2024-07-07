from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

url_wiki: str = 'https://secure-retreat-92358.herokuapp.com/'
driver.get(url_wiki)

first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
button = driver.find_element(By.XPATH, '/html/body/form/button')

first_name.send_keys('Carlos')
last_name.send_keys('Monteiro')
email.send_keys('sadbshajdb@bhafbhj.com')
button.click()
