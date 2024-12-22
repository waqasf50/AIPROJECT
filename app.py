from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model and encoder
with open('model.pkl', 'rb') as f:
    model, label_encoder = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        year = int(data['year'])
        brand = data['brand'].lower()
        mileage = float(data['mileage'])

        # Encode the brand
        brand_encoded = label_encoder.transform([brand])[0]

        # Make prediction
        features = np.array([[year, brand_encoded, mileage]])
        prediction = model.predict(features)[0]

        return jsonify({
            'predicted_price': round(prediction, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)