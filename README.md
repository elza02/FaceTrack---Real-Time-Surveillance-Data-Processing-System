TO RUN THE APP,

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
