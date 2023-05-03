import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("", "")

    mesaj = MIMEMultipart()
    mesaj["From"] = ""           # Gönderen
    mesaj["Subject"] = ""    
    body = """

    Python ile email gönderiyorum.

    """

    body_text = MIMEText(body, "plain")
    mesaj.attach(body_text)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail başarılı bir şekilde gönderildi.")
    mail.close()


except:
    print("Hata:", sys.exc_info()[0])