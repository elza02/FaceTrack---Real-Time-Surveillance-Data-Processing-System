## Overview
FaceTrack is a real-time surveillance data processing system that leverages facial recognition technology using Apache Spark and the Kafka framework. The primary objective of the system is to collect traffic data from a real-time facial recognition API, continuously analyze it, and provide immediate information on identified individuals. This project aims to enhance surveillance capabilities and improve public safety through advanced data processing techniques.

## Features
- **Real-Time Data Processing:** Continuously collects and processes data from a facial recognition API.
- **Scalable Architecture:** Built on Apache Spark and Kafka, allowing for efficient handling of large data streams.
- **Facial Recognition Integration:** Utilizes advanced algorithms to identify individuals in real time.
- **Traffic Data Analysis:** Provides insights into traffic patterns and identified individuals, contributing to improved urban safety.

## Technologies Used
- **Apache Spark:** For distributed data processing and analytics.
- **Kafka:** For real-time data streaming and message brokering.
- **Facial Recognition API:** To capture and analyze traffic data.
- **Java/Python:** Programming languages used for development.


## TO RUN THE APP,

  1. Zookepper and Kafka
    - run terminal
    - cd yourPath/kafka
    - run:
        * .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties (to run zookeeper)
        * .\bin\windows\kafka-server-start.bat .\config\server.properties (to run kafka server)
        * .\bin\windows\kafka-topics.bat --create --topic imageTest --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 (create frst topic)
        * .\bin\windows\kafka-topics.bat --create --topic prediction-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 (create frst topic)
    - run other terminal
        * ./gradlew bootRun (to run spring boot) 
