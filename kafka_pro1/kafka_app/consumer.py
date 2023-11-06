from kafka import KafkaConsumer
import json
from .views import GetInput

topic_name = 'location'
consumer = KafkaConsumer(topic_name,bootstrap_servers=['localhost:9093','localhost:9094','localhost:9095'],
                         value_deserializer=lambda z: json.loads(z.decode('utf-8')),auto_offset_reset='latest')

name = GetInput()
for message in consumer:
    if message.value['name'] == name.request.POST:
        print(message.value)
