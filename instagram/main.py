from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

INSTA_USERNAME = "divineframes.ig"
INSTA_PASSWORD = "Akhil@2006"


class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://m.instagram.com/accounts/login/")
        time.sleep(6)         

        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")

        username.send_keys(INSTA_USERNAME)
        password.send_keys(INSTA_PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        print("Logged in successfully!")

    def search(self):
     all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
     for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/varun.aditya/followers")
        time.sleep(8.2)
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

bot = InstagramBot()
bot.login()
bot.find_followers()
bot.search()