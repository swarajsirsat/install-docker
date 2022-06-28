import os.path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
sender_email = "swarajsirsat677@gmail.com"
receiver_email = "aabhi4460singh@gmail.com"
password = "lcaekixqdmtihupg"
SUBJECT = 'test email'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = SUBJECT
TEXT = 'This is my message'
msg.attach(MIMEText(TEXT, 'plain'))

file_location = '/export-members/export-all.csv'
filename = 'export-all.csv'

attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email,password)
text = msg.as_string()
server.sendmail(sender_email, receiver_email, text)
server.quit()
