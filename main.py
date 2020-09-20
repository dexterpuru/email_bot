# import os
import smtplib
import imghdr
from secrets import ps, add
from email.message import EmailMessage

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = "Pratyaksh's email bot"
msg['From'] = add
msg['To'] = 'pratyaksh2000saini@gmail.com'
msg.set_content('01001000 01100101 01101100 01101100 01101111 00100001')

with open('anime1.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image',
                   subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(add, ps)
    smtp.send_message(msg)
