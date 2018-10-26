import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

consumer = KafkaConsumer(bootstrap_servers=['172.24.41.165:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(pattern='.*.-Usaquen-.*.*')

producer = KafkaProducer(bootstrap_servers=['172.24.41.165:8081'], 
             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

server = smtplib.SMTP()
server.connect("pruebaarquisoft1@gmail.com", 587)
server.starttls()
server.login("pruebaarquisoft1@gmail.com", "prueba123")

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
        pago = message.value["valorAPagar"]
        mensaje = 'Se realizo una reserva en su parqueadero de ' + place + ' por COP ' + str(pago) +  '. Fecha de reserva: ' + fechares + ', fecha de inicio reserva: ' + fechain  + ', fecha fin reserva: ' + fechafin + '. Hora llegada carro: ' + horlle + ', hora salida carro: ' + horsal 
        print(mensaje)
        msg = MIMEMultipart()
        msg['From'] = 'Nidoo Servicios <pruebaarquisoft1@gmail.com>' # Note the format
        msg['To'] = '%s <' + correo +'>'
        msg['Subject'] = 'Se realizo una reserva en su parqueadero de %s' % "Nidoo"
        msg.attach(MIMEText(mensaje))
        server.sendmail("pruebaarquisoft1@gmail.com", correo , msg.as_string())
        print(correo)
        
        
    except:
        pass


server.quit()
