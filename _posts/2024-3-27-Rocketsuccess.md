---
title: Rocket Simulator
layout: post
permalink: /predict
description: Rocket Simulator
type: tangibles
courses: { compsci: { week: 3 } }
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rocket Launch Data Input</title>
</head>
<body>
    <h1>Rocket Launch Data Input</h1>
    <form action="/predict" method="post">
        <label for="origin_country">Origin Country:</label>
        <input type="text" id="origin_country" name="origin_country" required><br><br>
        <label for="payload_mass">Payload Mass (kg):</label>
        <input type="number" id="payload_mass" name="payload_mass" required><br><br>
        <label for="company">Company:</label>
        <input type="text" id="company" name="company" required><br><br>
        <label for="engine_strength">Engine Strength:</label>
        <input type="text" id="engine_strength" name="engine_strength" required><br><br>
        <input type="submit" onclick="predict_rocket_success()">
    </form>
</body>
    <script>
        function predict_rocket_success() {
            var form = document.getElementById('rocketForm');
            var formData = new FormData(form);
            fetch('http://127.0.0.1:8082/api/rocketsuccess/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(Object.fromEntries(formData))
            })
            .then(response => response.json())
            .then(data => {
                var resultDiv = document.getElementById('result');
                resultDiv.innerHTML = '<h2>Prediction Result</h2>';
                for (var key in data) {
                    resultDiv.innerHTML += '<p>' + key + ': ' + data[key] + '</p>';
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    </script>
</body>







