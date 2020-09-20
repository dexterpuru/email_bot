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

msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color: SlateGrey;">This is auto generated Email!</h1>
        </body>
    </html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(add, ps)
    smtp.send_message(msg)
