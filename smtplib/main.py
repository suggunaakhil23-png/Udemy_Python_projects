import smtplib

my_email = "suggunaakhil@gmail.com"
password = "zhqhseysgsdfcuto"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="akhilpraveena2006@gmail.com",
    msg="Subject: Test\n\nHello"
)
connection.close()
