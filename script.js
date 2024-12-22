document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Get form values
    const year = parseInt(document.getElementById('year').value);
    const mileage = parseInt(document.getElementById('mileage').value);
    const brand = document.getElementById('brand').value;
    
    try {
        // Send prediction request to Flask backend
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                year: year,
                mileage: mileage,
                brand: brand
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        // Display result
        document.getElementById('result').classList.remove('hidden');
        document.getElementById('prediction').textContent = 
            `$${data.predicted_price.toLocaleString()}`;
            
    } catch (error) {
        alert('Error: ' + error.message);
    }
});