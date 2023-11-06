from django.shortcuts import render
from .serializer import InputSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from kafka import KafkaConsumer
import json
from .producer import producer1


topic_name = 'location'
consumer = KafkaConsumer(topic_name,bootstrap_servers=['localhost:9093','localhost:9094','localhost:9095'],
                         value_deserializer=lambda z: json.loads(z.decode('utf-8')),auto_offset_reset='latest')


class GetInput(CreateAPIView):
    serializer_class = InputSerializer

    def post(self, request, *args, **kwargs):
        # serializer_class = InputSerializer(data=request.data)

        try:
            name = request.data['name']
            for message in consumer:
                if message.value['name'] == name:
                    print(message.value)

            return Response({'status': 'success',
                             'input': name,
                             })
        except:
            return Response({'status':'Failed'})
        # if serializer_class.is_valid():
        # for message in consumer:
        #     if message.value['name'] == name:
        #         print(message)


class ProduceData(APIView):

    def get(self,request):
        result = producer1()
        return Response({'status':'success',
                         'created_data': result})
