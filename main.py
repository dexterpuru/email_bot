# import os
import smtplib
from secrets import ps, add

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(add, ps)

    subject = "Dinner this weekend?"
    body = "Wanna grab dinner this weekend at Wendy's?"

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(add, 'pratyaksh2000saini@gmail.com', msg)
