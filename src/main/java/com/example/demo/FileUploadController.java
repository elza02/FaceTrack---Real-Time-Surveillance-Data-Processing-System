package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

@Controller
public class FileUploadController {

    @Autowired
    private KafkaTemplate<String, byte[]> kafkaTemplate;

    @Autowired
    private PredictionService predictionService;

    private final String topic = "imageTest";
    private final String imageFolder = "src/main/resources/static/uploaded_images";

    @GetMapping("/")
    public String index() {
        return "index";
    }

    @GetMapping("/processing")
    public String processing(@RequestParam("imageName") String imageName, Model model) {
        model.addAttribute("imageName", imageName);
        return "processing";
    }

    @GetMapping("/result")
    public String result(@RequestParam("imageName") String imageName, Model model) {
        String prediction = predictionService.getLatestPrediction();
        model.addAttribute("imageName", imageName);
        model.addAttribute("prediction", prediction);
        return "result";
    }

    @PostMapping("/upload")
    public String handleFileUpload(@RequestParam("file") MultipartFile file,
                                   RedirectAttributes redirectAttributes) throws IOException {
        // Create the directory if it does not exist
        Path uploadPath = Paths.get(imageFolder);
        if (!Files.exists(uploadPath)) {
            Files.createDirectories(uploadPath);
        }

        // Save the image to the local file system
        byte[] bytes = file.getBytes();
        Path path = uploadPath.resolve(file.getOriginalFilename());
        Files.write(path, bytes);
        //kafkaTemplate.send(topic, file.getOriginalFilename(), bytes);
        kafkaTemplate.send(topic, bytes);


        //redirectAttributes.addFlashAttribute("message", "File uploaded successfully");
        predictionService.waitForPrediction(); // Wait for the prediction to be received
        return "redirect:/result?imageName=" + file.getOriginalFilename();
    }
}
