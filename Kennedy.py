import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.ehlo() # To start the connection
server.login("pruebaarquisoft1@gmail.com", "prueba123")

consumer = KafkaConsumer(bootstrap_servers=['172.24.41.165:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(pattern='.*.-Kennedy-.*.*')

producer = KafkaProducer(bootstrap_servers=['172.24.41.165:8081'], 
             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for message in consumer:
    try:
        print(message.value.demandante)
        
    except:
        pass

