import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform

consumer = KafkaConsumer(bootstrap_servers=['172.24.41.165:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(pattern='.*.-Kennedy-.*.*')

producer = KafkaProducer(bootstrap_servers=['172.24.41.165:8081'], 
             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

temp_list1 = []
temp_list2 = []

sum = 0
for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    print(type(message.value))
#    if (message.value['place'] == "piso2/cuarto1"):
#      temp_list1.append(message.value['value'])
#    elif (message.value['place'] == "piso2/cuarto2"):
#      temp_list2.append(message.value['value'])
#
#    if len(temp_list1) == 6:
#      for i in range(0,len(temp_list1)):
#        sum=sum+temp_list1[i]
#      temp_list1 = []
#      sum = 0




