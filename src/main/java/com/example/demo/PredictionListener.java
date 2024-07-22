package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class PredictionListener {

    @Autowired
    private PredictionService predictionService;

    @KafkaListener(topics = "prediction-topic", groupId = "group_id")
    public void listen(String message) {
        predictionService.setLatestPrediction(message);
    }
}
