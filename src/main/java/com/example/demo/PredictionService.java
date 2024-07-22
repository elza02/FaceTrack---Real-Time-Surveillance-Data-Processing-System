package com.example.demo;

import org.springframework.stereotype.Service;

@Service
public class PredictionService {

    private String latestPrediction;
    private final Object lock = new Object();

    public void setLatestPrediction(String prediction) {
        synchronized (lock) {
            this.latestPrediction = prediction;
            lock.notifyAll();
        }
    }

    public String getLatestPrediction() {
        synchronized (lock) {
            return latestPrediction;
        }
    }

    public void waitForPrediction() {
        synchronized (lock) {
            try {
                lock.wait(19000); // Wait for up to 10 seconds
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}
