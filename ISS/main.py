import requests
import math
import smtplib
import time
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user="suggunaakhil@gmail.com", password="zhqhseysgsdfcuto")

my_lat = 17.4065
my_long = 78.4772

iss = requests.get("http://api.open-notify.org/iss-now.json")
data = iss.json()

lat = float(data["iss_position"]["latitude"])
long = float(data["iss_position"]["longitude"])

def distance_km(lat1, lon1, lat2, lon2):
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    R = 6371
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    return R * c

a = distance_km(my_lat, my_long, lat, long)
print(a)
while True :
  time.sleep(60)
  if a < 100000:
    connection.sendmail(
        from_addr="suggunaakhil@gmail.com",
        to_addrs="gireeshreddy006@gmail.com",
        msg=f"Subject: ISS Overhead Alert\n\n"
            f"The ISS is near your location.\n\n"
            f"Distance: {a:.2f} km\n\n"
            f"- Akhil"
    )
    print("Message Sent")

connection.close()
