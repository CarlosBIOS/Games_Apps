# Se quiser criar um exel, então posso usar o Google forms. Como fiz neste projeto:
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScappingWeb:
    header: dict = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84"
                      ".0.4147.125 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    request = requests.get('https://appbrewery.github.io/Zillow-Clone/', headers=header)
    request.raise_for_status()

    def __init__(self):
        self.soup = BeautifulSoup(self.request.text, 'html.parser')
        self.data_dict: dict = {}

    def extract(self):
        all_data_rent = self.soup.find_all(class_='PropertyCardWrapper__StyledPriceLine', name='span')
        rent: list = [data.text[:6] if ',' in data.text else data.text[:5] for data in all_data_rent]

        all_data_address = self.soup.find_all(name='address')
        address = [data.text.strip() for data in all_data_address]

        all_data_urls = self.soup.find_all(name='a', class_='property-card-link')
        urls = [data.get('href') for data in all_data_urls]

        for i in range(len(rent)):
            self.data_dict[i] = (address[i], rent[i], urls[i])

        return self.data_dict


class DocForm:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument("--start-maximized")

    def __init__(self, data_dict):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.URL: str = ('https://docs.google.com/forms/d/e/1FAIpQLSc4emwlriTqYBsSE96ewLOVqHgBCdLwkTa-Bfv0PJo8uCwrKw/vi'
                         'ewform?usp=sf_link')
        self.data_dict: dict = data_dict

    def doc_form_google(self):
        for _, values in self.data_dict.items():
            self.driver.get(self.URL)

            time.sleep(0.5)
            address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/'
                                                         'div/div[1]/div/div[1]/input')
            address.send_keys(values[0])

            price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/'
                                                       'div[1]/div/div[1]/input')
            price.send_keys(values[1])

            link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/'
                                                      'div[1]/div/div[1]/input')
            link.send_keys(values[2])

            button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            button.click()

        self.driver.close()


if __name__ == '__main__':
    scrapping_web = ScappingWeb()
    dict_data = scrapping_web.extract()

    docform = DocForm(dict_data)
    docform.doc_form_google()

