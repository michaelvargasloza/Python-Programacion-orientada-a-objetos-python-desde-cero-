#Envío de correos.
import smtplib
from email.mime.text import MIMEText

username = input("Escribe tu correo: ")
password = input("Escribe tu contraseña: ")
targets = input("Introduce el destino: ")
asunto = input("Escribe el asunto del correo: ")
msg = input("Escribe el texto del correo: ")

#Enviado del correo
msg = MIMEText(msg)
msg['Subject'] = (asunto)
msg['From'] = username
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL('Host', 'Puerto')
server.login(username, password)
server.sendmail(username, targets, msg.as_string())
server.quit()