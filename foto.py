################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os

mytext='Sonrie para la foto '
os.system("pico2wave -l es-ES -w L.wav \""+mytext+"\"")
os.system("aplay L.wav")

subprocess.call(['fswebcam', 'vozraspi.jpg'])
print('tomando foto')
email_sender = 'ttoscanoqui@gmail.com'
email_receiver = 'ttoscano@espol.edu.ec'
subject = 'VOzRaspi'
msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject']= subject
body = 'Prueba de foto'
msg.attach(MIMEText(body, 'plain'))

#FILE PART
filename = 'vozraspi.jpg'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet_stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= '+filename)
msg.attach(part)
#########

text = msg.as_string()
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(email_sender, 'TONNY01012018')
connection.sendmail(email_sender, email_receiver, text )
connection.quit()


mytext='foto enviada revisa tu correo '
os.system("pico2wave -l es-ES -w L.wav \""+mytext+"\"")
os.system("aplay L.wav")
