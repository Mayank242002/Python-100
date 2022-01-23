import smtplib
import datetime as dt
import random


now=dt.datetime.now()
week=now.weekday()
file=open("day-32-smtplib/quotes.txt","r")
file_content=file.readlines()
random_quote=random.choice(file_content)
random_quote=random_quote.encode('utf-8')


my_email="msngi24july@gmail.com"

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password="mayank@1234")
if week==5:
    connection.sendmail(
    from_addr=my_email,
    to_addrs="negi.mayanksingh.2016850@gmail.com",
    msg=random_quote)


connection.close()



