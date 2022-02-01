import smtplib
import datetime as dt
import random

my_email = '__put your email here__'
password = "__put your password here__"
friends_email = "__put yur friends email here__"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=friends_email,
            msg=f"Subject: Monday Motivation \n\n Today's quote: \n {quote}"
        )
