import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/Apple-iPhone-14-256GB-Starlight/dp/B0BDJS3MRM"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive"
}


response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price_tag = soup.find("span", class_="a-price-whole")

if not price_tag:
    print("Price not found. Amazon blocked request or selector changed.")
    quit()

price_text = price_tag.get_text(strip=True).replace(",", "")

print("Current Price:", price_text)

TARGET_PRICE = "60000"

if price_text <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user="your_email@gmail.com", password="your_app_password")
        connection.sendmail(
            from_addr="your_email@gmail.com",
            to_addrs="akhilpraveena2006@gmail.com",
            msg=f"Subject:Price Alert!\n\nPrice dropped to ₹{price_text}"
        )
        print("Email sent!")
