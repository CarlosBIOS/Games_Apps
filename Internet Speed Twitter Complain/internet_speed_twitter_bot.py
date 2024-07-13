from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import getenv
import time


class InternetSpeedTwitterBot:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument("--start-maximized")

    def __init__(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down: str = '0'
        self.up: str = '0'

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')

        time.sleep(1)

        accept_button = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        accept_button.click()

        go_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        go_button.click()

        time.sleep(47)

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                       '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/'
                                                       'span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                     'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/'
                                                     'span').text

    def tweet_at_provider(self):
        self.driver.get('https://x.com/i/flow/login')

        time.sleep(3)

        email_text = self.driver.find_element(By.NAME, 'text')
        email_text.send_keys(getenv('twitter_email'), Keys.ENTER)

        time.sleep(1)

        password_text = self.driver.find_element(By.NAME, 'password')
        password_text.send_keys(getenv('twitter_password'), Keys.ENTER)

        time.sleep(5)

        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                   'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/'
                                                   'div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/'
                                                   'div/div/div/div')
        tweet.send_keys('oi')
