import datetime as dt
import random
import pandas as pd
import smtplib

EMAIL = "<your email>"
PASSWORD = "<your password>"

as_of_now = dt.datetime.now()
birthday_month = as_of_now.month
birthday_date = as_of_now.day

data = pd.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")

for i in birthday_data:
    if i["month"] == birthday_month and i["day"] == birthday_date:
        random_letter = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_letter}.txt") as file:
            letter = file.read()
            send_letter = letter.replace("[NAME]", i["name"])
            email_to = i["email"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=email_to,
                msg=f"subject:Happy Birthday\n\n{send_letter}"
            )
