# Made with ❤️ by ソヌ
# Automating cold emails, the smart way.
from pickle import format_version
from timeit import template
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import pandas as pd
from token import AT

with open("application.txt", "r") as file:
    content = file.read()

# Load env vars from .env file
load_dotenv()

# Pull values from environment
sender_email = os.getenv("SENDER_EMAIL")
sender_data = pd.read_csv("data.csv")
display_name = os.getenv("DISPLAY_NAME")
# receiver_email = os.getenv("RECEIVER_EMAIL")

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT"))  # Don't forget to cast it to int
username = os.getenv("SMTP_USERNAME")
password = os.getenv("SMTP_PASSWORD")


for index , row in sender_data.iterrows():
    email = row['email']
    name = row['name']
    company = row['company']

# Compose the email
    message = MIMEMultipart()
    message["From"] = f"{display_name} <{sender_email}>"
    message["To"] = email
    message["Subject"] = f"Application for Internship Opportunity."

    # Email body
    body = content.format(name=name, sender_email=sender_email, domain="Backend Development", company_name=company)
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect and send
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
        print(f"✅ Email sent to {email} successfully!")
    except Exception as e:
        print(f"❌ Failed to send email to {email}: {str(e)}")
