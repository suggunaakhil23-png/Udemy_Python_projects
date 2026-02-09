from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

prices = []
link1 = []
add = []
class Listings:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def add(self):
        self.driver.get("https://appbrewery.github.io/Zillow-Clone/")
        time.sleep(1)
        lin = self.driver.find_elements(By.CSS_SELECTOR,value=".StyledPropertyCardDataArea-anchor")
        for link in lin:
         addr = link.text
         add.append(addr)
         links = link.get_attribute("href")
         link1.append(links)
        price = self.driver.find_elements(By.CSS_SELECTOR,value=".PropertyCardWrapper__StyledPriceLine")
        for pri in price:
         p = pri.text
         prices.append(p)
    
    def fill_google(self):
       for i in range(len(prices)):
          self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSezkJFzGd9AAEnjHxBiHp5VeagBH0VaSWGW4AOyzqUtgMlUeQ/viewform?usp=publish-editor")
          addr = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[1]"))
            )
          addr.click()
          addr.send_keys(add[i])
          price = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
            )
          price.click()
          price.send_keys(prices[i])
          link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
            )
          link.click()
          link.send_keys(link1[i])
          button = self.driver.find_element(By.XPATH,value = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
          button.click()

bot = Listings()
bot.add()
bot.fill_google()