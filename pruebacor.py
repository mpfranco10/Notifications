import smtplib
from Kennedy.py import *


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("pruebaarquisoft1@gmail.com", "prueba123")
 

msg = "moshi moshi hi hello!"
server.sendmail("pruebaarquisoft1@gmail.com", "pruebaarquisoft1@hotmail.com", msg)
server.quit()


while True:
    print("el elemento sacado ")
    print(content[0])
    content.remove(content[0]);
