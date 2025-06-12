import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load env vars from .env file
load_dotenv()

# Pull values from environment
sender_email = os.getenv("SENDER_EMAIL")
display_name = os.getenv("DISPLAY_NAME")
receiver_email = os.getenv("RECEIVER_EMAIL")

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT"))  # Don't forget to cast it to int
username = os.getenv("SMTP_USERNAME")
password = os.getenv("SMTP_PASSWORD")

# Compose the email
message = MIMEMultipart()
message["From"] = f"{display_name} <{sender_email}>"
message["To"] = receiver_email
message["Subject"] = f"{display_name}"

# Email body
body = "Hello vaii!!!"
message.attach(MIMEText(body, "plain"))

try:
    # Connect and send
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Failed to send email:", str(e))
