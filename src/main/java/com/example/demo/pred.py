import os
from kafka import KafkaConsumer, KafkaProducer
from PIL import Image
from io import BytesIO
import numpy as np
import model
import os

IMAGE_FOLDER = 'C:\\Users\\dell\\Desktop\\MS_DS\\M2\\AppAutomaique\\Projet\\projet_sb_kafka\\demo\\src\\main\\resources\\static\\uploaded_images\\'




# Kafka consumer setup
consumer = KafkaConsumer(
    'imageTest',
    bootstrap_servers='localhost:9092',
    group_id='group_id'
)
import json
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Consume messages from Kafka
for message in consumer:
    #image_name = message.key.decode('utf-8')
    #print(image_name)
    image_bytes = message.value
    prediction = model.search_for_nearest_vect(image_bytes)
    print(prediction)
    #prediction = model.predict(IMAGE_FOLDER + image_name)
    producer.send('prediction-topic', prediction)
