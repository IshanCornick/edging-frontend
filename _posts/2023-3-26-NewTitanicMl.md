---
toc: true
comments: false
layout: post
title: New ML
description: Example Blog!!!  This shows planning and notes from hacks.
type: plans
courses: { compsci: {week: 0} }
---

<body>
    <h1>Titanic Survival Predictor</h1>
    <form id="titanicForm">
        <div class="form-group">
            <label for="_title">Job Title:</label>
            <input type="text" id="_title" name="_title" class="form-control" required>
        </div>
        <div class="form-group">
            <label for="_field">Field:</label>
            <input type="text" id="_field" name="_field" class="form-control" required>
        </div>
        <div class="form-group">
            <label for="_qualification">Qualification:</label>
            <input type="text" id="_qualification" name="_qualification" class="form-control" required>
        </div>
        <div class="form-group">
            <label for="_pay">Pay:</label>
            <input type="text" id="_pay" name="_pay" class="form-control" required>
        </div>
        <button type="button" class="btn btn-primary" onclick="predictSurvival()">Predict Survival</button>
    </form>
    <div id="result"></div>
    <script>
        function predictSurvival() {
            var form = document.getElementById('titanicForm');
            var formData = new FormData(form);
            fetch('http://127.0.0.1:8082/api/titanic/predict', {
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

