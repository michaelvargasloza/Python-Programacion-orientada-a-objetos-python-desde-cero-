#Envío de correos.
import smtplib

username = input("Escribe tu correo: ")
password = input("Escribe tu contraseña: ")
destinatario = ("Introduce el destino: ")
msg = input("Escribe el texto del correo: ")

server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
server.starttls()
server.login(username, password)
server.sendemail(username, destinatario, msg)
server.quit()