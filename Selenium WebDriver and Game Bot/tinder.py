from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from os import getenv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

URL: str = 'https://tinder.com'
driver.get(URL)

# language = driver.find_element(By.XPATH, '//*[@id="t-1686761967"]/div/div/div[3]/button/svg/path')
# language.click()

time.sleep(0.5)

criar_conta = driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/button')
criar_conta.click()

time.sleep(0.5)

facebook_button = driver.find_element(By.XPATH, '//*[@id="t-1686761967"]/div/div[1]/div/div[1]/div/div/div[2]/'
                                                'div[2]/span/div[2]/button')
facebook_button.click()

time.sleep(0.5)

base_window = driver.window_handles[0]  # window_handles → Permite ver quantas páginas estão abertas!!!
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

button_permission = driver.find_element(By.XPATH, '//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/'
                                                  'div[2]/div/div[2]/div[1]/div/div[1]/div/span/span')
button_permission.click()

email_button = driver.find_element(By.XPATH, '//*[@id="email"]')
email_button.send_keys(getenv('email_facebook'))

password_button = driver.find_element(By.NAME, 'pass')
password_button.send_keys(getenv('password_facebook'))

iniciar_sessao = driver.find_element(By.NAME, 'login')
iniciar_sessao.click()

time.sleep(7)

driver.switch_to.window(base_window)
print(driver.title)
