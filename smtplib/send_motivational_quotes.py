import datetime as dt
import smtplib
import random

motivational_quotes = [
    "Believe in yourself and all that you are.",
    "Dream big. Work hard. Stay focused.",
    "Success doesn’t come to you, you go to it.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Small steps every day lead to big results.",
    "Push yourself, because no one else will.",
    "Consistency is more important than motivation.",
    "Your future is created by what you do today.",
    "Hard work beats talent when talent doesn’t work hard.",
    "Stay disciplined and trust the process."
]

my_email = "suggunaakhil@gmail.com"
password = "zhqhseysgsdfcuto"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    now = dt.datetime.now()
    day = now.weekday()   

    if day == 6:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="akhilpraveena2006@gmail.com",
            msg=f"Subject: Today's Motivation\n\n{random.choice(motivational_quotes)}"
        )
