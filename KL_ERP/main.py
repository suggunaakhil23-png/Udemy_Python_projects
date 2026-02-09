from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from PIL import Image
from twocaptcha import TwoCaptcha
import io
import time
import os

solver = TwoCaptcha("5f421e79d72272b9e86cd7aa174225d1")

username = 2410040134
password = "akhil2006"

class erp:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get("https://newerp.kluniversity.in/")
        self.driver.find_element(By.XPATH,'//*[@id="loginFormUserNameID"]').send_keys(username)
        self.driver.find_element(By.XPATH,'//*[@id="loginFormPasswordID"]').send_keys(password)

        img = self.driver.find_element(By.ID,"loginFormCaptcha-image")
        src = img.get_attribute("src")
        if src.startswith("/"):
            src = "https://newerp.kluniversity.in" + src

        cookies = {c['name']:c['value'] for c in self.driver.get_cookies()}
        img_bytes = requests.get(src, cookies=cookies).content
        Image.open(io.BytesIO(img_bytes)).save("cap.png")

        result = solver.normal("cap.png")
        text = result["code"]

        self.driver.find_element(By.XPATH,"//input[contains(@id,'Captcha') or contains(@name,'captcha')]").send_keys(text)
        self.driver.find_element(By.XPATH,'//*[@id="login-form"]/div[7]/div/button').click()
        time.sleep(5)

bot = erp()
bot.login()
