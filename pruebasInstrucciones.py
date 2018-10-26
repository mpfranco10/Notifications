#generar el topic de prueba
#sudo /opt/Kafka/bin/kafka-topics.sh --create --zookeeper localhost:8080 --replication-factor 1 --partitions 1 --topic test  Se crea el topic
#sudo /opt/Kafka/bin/kafka-console-producer.sh --broker-list localhost:8081 --topic test  Se genera un productor por consola
#sudo /opt/Kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:8081 --from-beginning -topic test --partition 0 Se crea un consumidor por consola
#Se corre el productor y el consumidor y en otra consola se procede a hacer las pruebas de carga.
#Instrucciones para pruebas de carga


#Para el productor
# sudo /opt/Kafka/bin/kafka-producer-perf-test.sh --topic test --num-records 1500 --record-size 250 --throughput 1500 --producer-props acks=1 bootstrap.servers=localhost:8081

#Para el consumidor
# sudo /opt/Kafka/bin/kafka-consumer-perf-test.sh --topic Suba-Pasadena-calle134-IvanDuque --broker-list localhost:8081 --messages 100 --threads 20




