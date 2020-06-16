#Envío de correos
import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = '' #Salida
smtp_ssl_port = #Puerto
#Datos de usuario.
username = '' #Usuario
password = '' #Pass
sender = '' #Remitente
#Datos del receptor(es).
targets = ['']

#Enviado del correo
msg = MIMEText('Hola mundo!')
msg['Subject'] = ('Asunto.')
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()