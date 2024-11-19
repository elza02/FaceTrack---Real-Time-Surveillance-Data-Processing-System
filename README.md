# FaceTrack: Real-Time Surveillance with Facial Recognition

## Overview

**FaceTrack** is an advanced real-time surveillance data processing system that integrates cutting-edge facial recognition technology with the power of Apache Spark and Kafka. The system is designed to continuously collect, analyze, and respond to traffic data from a real-time facial recognition API, delivering instant identification insights. By harnessing scalable data processing techniques, FaceTrack enhances urban surveillance capabilities, improving both public safety and operational efficiency in real-time monitoring scenarios.

The system not only tracks and identifies individuals but also offers valuable insights into traffic and pedestrian patterns, helping authorities and organizations make informed decisions to strengthen security measures in high-traffic areas.

## Key Features
- **Real-Time Data Streaming and Processing**: Continuously ingests and processes facial recognition data, ensuring timely identification and response.
- **Scalable, Distributed Architecture**: Built using Apache Spark and Kafka to efficiently manage and scale large volumes of streaming data.
- **Facial Recognition Integration**: Employs sophisticated facial recognition algorithms to detect and identify individuals in real-time.
- **Traffic and Behavioral Analysis**: Provides actionable insights on traffic patterns and identified individuals, contributing to enhanced public safety and smarter city management.

## Technologies Used
- **Apache Spark**: Powers the distributed data processing and advanced analytics, allowing the system to handle large-scale data in real time.
- **Kafka**: Ensures high-throughput, fault-tolerant real-time data streaming and message brokering between components.
- **Facial Recognition API**: Captures and processes facial data from traffic and surveillance sources.
- **Java/Python**: Core languages used to develop and integrate the system’s components for maximum performance and flexibility.

## How to Run the Application

### Prerequisites:
Ensure you have Apache Zookeeper, Kafka, and a working setup of the application environment.

### Steps to Set Up and Run:
1. **Start Zookeeper and Kafka**
    - Open a terminal and navigate to your Kafka installation directory:
      ```bash
      cd yourPath/kafka
      ```
    - Start Zookeeper:
      ```bash
      .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
      ```
    - Start the Kafka server:
      ```bash
      .\bin\windows\kafka-server-start.bat .\config\server.properties
      ```
    - Create Kafka topics:
      - For image processing:
        ```bash
        .\bin\windows\kafka-topics.bat --create --topic imageTest --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
        ```
      - For predictions:
        ```bash
        .\bin\windows\kafka-topics.bat --create --topic prediction-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
        ```

2. **Run the Application**
    - In another terminal, navigate to the project directory and run the Spring Boot application:
      ```bash
      ./gradlew bootRun
      ```

The application should now be up and running, processing real-time data streams through Kafka and Spark, while interacting with the facial recognition API to deliver instant insights.
