import json

import confluent_kafka
from kafka import KafkaConsumer

from db_module import send_data
from redis_module import save_data

import requests





         
conf = {'bootstrap.servers': 'rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091',
        'group.id': 'cosco_2112',
        'auto.offset.reset': 'latest',
        'security.protocol': 'SASL_SSL',
        'ssl.ca.location': 'C:\InfluxData\py\cacert.pem',
        'enable.ssl.certificate.verification': True,
        'sasl.mechanisms': "SCRAM-SHA-512",
        'sasl.username': "9433_reader",
        'sasl.password': "eUIpgWu0PWTJaTrjhjQD3.hoyhntiK"

        }

consumer = confluent_kafka.Consumer(conf)

consumer.subscribe(['zsmk-9433-dev-01'])


while True:
    msg = consumer.poll(1.0)

    if msg is None:
        print("continue")
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))

    val = msg.value().decode('utf-8')
    # print(json.loads(val))

    send_data(json.loads(val))
    save_data(json.loads(val))
    
    requests.request("GET", "http://127.0.0.1:4242/new")
    print("Send")