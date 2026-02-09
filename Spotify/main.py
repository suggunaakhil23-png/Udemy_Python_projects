import requests
from bs4 import BeautifulSoup

date = input("What year do you want to travel to? YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
print(soup.prettify())
