# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv
import datetime as dt
import os
import smtplib
import random

load_dotenv()
sender_email = os.getenv("EMAIL")
password = os.getenv("DOMAIN_PW")
file_path = './quotes.txt'  # Replace with the actual path to your .txt file

try:
    with open(file_path, 'r') as file:
        # Read and print the content
        quotes = file.readlines()
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)


def send_motivation(quote):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user = sender_email, password = password)
        connection.sendmail(from_addr = sender_email,
                            to_addrs="recipients_email@gmail.com",
                            msg=f"Subject:Motivation\n\n{quote}"
                            )


now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 3:    # 0 is Monday
    send_motivation(random.choice(quotes))
