from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "suggunaakhil@gmail.com"
TWITTER_PASSWORD = "xi^^kW?DSd+q=S6"
driver_path = r"C:\Users\akhil\Downloads\chromedriver-win32\chromedriver-win32"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".start-button a").click()
        time.sleep(60)
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed").text
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed").text
        print(self.up, self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        wait = WebDriverWait(self.driver, 40)

        email = wait.until(EC.presence_of_element_located((By.NAME, "text")))
        email.send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, "//span[text()='Next']/ancestor::button").click()

        password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password.send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH, "//span[text()='Log in']/ancestor::div[@role='button']").click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Tweet text']")))
        tweet_compose = self.driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tweet text']")
        tweet = f"Hey Internet Provider, why is my internet speed {self.down} down / {self.up} up when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up?"
        tweet_compose.send_keys(tweet)

        post_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']")))
        post_button.click()

        time.sleep(3)
        self.driver.quit()

bot = InternetSpeedTwitterBot(driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()
