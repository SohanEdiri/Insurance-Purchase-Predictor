document.getElementById('predictionForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams(data),
        });

        const result = await response.json();

        if (result.status === 'success') {
            document.getElementById('result').textContent = `Prediction: ${result.prediction}`;
        } else {
            document.getElementById('result').textContent = `Error: ${result.message}`;
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Error: Unable to get prediction';
    }
});

