import smtplib
from Kennedy.py import *


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("pruebaarquisoft1@gmail.com", "prueba123")
 

while True:
    print("Enviando correo")
    
    if content[0] is not None:
        msg = "moshi moshi hi hello!"
        server.sendmail("pruebaarquisoft1@gmail.com", "pruebaarquisoft1@gmail.com", msg)
        content.remove(content[0]);
    

server.quit()