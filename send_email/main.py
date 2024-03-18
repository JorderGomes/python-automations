import smtplib
import email.message
from dotenv import load_dotenv
import os

load_dotenv()

def send_email():
    message_body = '''
    Some lorem text.
    '''
    msg = email.message.Message()
    msg['subject'] = 'Assunto'
    msg['From'] = 'jordernoveau@gmail.com'
    msg['To'] = 'jorderpgomes@gmail.com'
    password =  os.getenv('EMAIL_PASSWORD')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(message_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

send_email()