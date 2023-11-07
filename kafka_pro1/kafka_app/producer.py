from kafka import KafkaProducer
import json
import time


def producer1():
    brokers = ['localhost:9093','localhost:9094','localhost:9095']
    producer = KafkaProducer(bootstrap_servers=brokers,
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    with open(r"C:\Users\Vrdella\Desktop\django-kafka\kafka_pro1\kafka_app\MOCK_DATA.json", 'r') as file:
        data = json.load(file)
        for datas in data:
            topic = 'location'
            producer.send(topic, value=datas)
            time.sleep(0.5)
