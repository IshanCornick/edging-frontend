<!DOCTYPE html>
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
        <input type="submit" value="Predict">
    </form>
</body>
</html>

<script>
document.getElementById('rocket_form').addEventListener('submit', function(event) {
    event.preventDefault(); 
    const formData = new FormData(this);


    const url = 'http://127.0.0.1:8082/api/rocketsuccessrate/predict';

    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction_result').innerHTML = `<h2>Prediction Result</h2><p>Success Percentage: ${data.success_percentage}</p>`;
    })
    .catch(error => console.error('Error:', error));
});
</script>