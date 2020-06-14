#Envío de correos
import smtplib

remitente = 'vargas_michael1993@yahoo.es'
destinatario = 'michael_vargas_loza@yahoo.es'
msg = 'Este es un correo enviado desde la consola de python.'

#Datos de usuario.
username = 'vargas_michael1993@yahoo.es'
password = ''

#Enviado del correo
server = smtplib.SMTP('smtp.mail.yahoo.com:587')
server.starttls()
server.login(username, password)
server.sendmail(remitente, destinatario, msg)
server.quit()