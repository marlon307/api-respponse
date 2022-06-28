import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def send_mail():
    # Email Address using to send from
    from_addr = os.getenv("EMAIL_TESTE")
    # Email Address to send to
    to_addr = os.getenv("EMAIL")

    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_addr
    # Email Subject
    msg["subject"] = "Subject"

    # Email Body
    body = "Email Body"
    msg.attach(MIMEText(body, "plain"))

    # Email Address using to send
    email = from_addr
    # Password for the email address using to send
    password = os.getenv("EMAIL_TESTE_PSW")
    # SMTP Set up
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(email, password)

    emailText = msg.as_string()
    mail.sendmail(from_addr, to_addr, emailText)

    mail.quit()
