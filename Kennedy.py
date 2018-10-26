import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

consumer = KafkaConsumer(bootstrap_servers=['172.24.41.165:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(pattern='.*.-Kennedy-.*.*')

producer = KafkaProducer(bootstrap_servers=['172.24.41.165:8081'], 
             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for message in consumer:
    try:
        correo = message.value["correoDemandante"]
        fechares = message.value["fechaReserva"]
        fechain = message.value["fechaInicio"]
        fechafin = message.value["fechaFin"]
        horlle = message.value["horaLlegada"]
        horsal = message.value["horaSalida"]
        place = message.value["lugar"]
        val = message.value["valorAPagar"]
        
        mensaje = '%s here is the email' + 'Se realizo una reserva en su parqueadero de ' + place + '. Fecha de reserva: ' + fechares + ', fecha de inicio reserva: ' + fechain  + ', fecha fin reserva: ' + fechafin + '. Hora llegada carro: ' + horlle + ', hora salida carro: ' + horsal + '. Valor a pagar: ' + val
        print(mensaje)
        
        
    except:
        pass

