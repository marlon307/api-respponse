import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def send_mail(
    title: str,
    destinatary: str or list[str],
    template_name: str,
    params: object,
) -> None:
    # Email Address using to send from
    from_addr = os.getenv("EMAIL_TESTE")
    # Email Address to send to
    to_addr = destinatary

    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_addr
    # Email Subject
    msg["subject"] = title

    # Email Body
    with open(
        os.path.dirname(__file__) + "/templates/%s" % template_name,
        "r",
        encoding="utf-8",
    ) as f:
        body = f.read().format(**params)

    msg.attach(MIMEText(body, "html"))

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
