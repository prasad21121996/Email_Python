import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['to'] = 'receiver email id '
email['from'] = 'sender name'
email['subject'] = 'email subject'

email.set_content('''Hi,

email

Thanks
 ''')


with smtplib.SMTP(host='smtp service like - smtp.gmail.com ',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email_id','password')
    smtp.send_message(email)
    print('Done')

