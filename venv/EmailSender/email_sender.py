import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text)
email = EmailMessage()
email['from'] = "John Doe"
email['to'] = '****@gmail.com'
email['subject'] = "Wallah~!! Tested Ok"

email.set_content(html.substitute({"name": "Mojo Jojo"}), html)

with smtplib.SMTP(host="smtp.gmail.com", port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('*****@gmail.com', '*********')
    smtp.send_message(email)
