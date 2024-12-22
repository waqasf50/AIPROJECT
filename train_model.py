import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the data
data = pd.DataFrame({
    'Year': [2018, 2019, 2020, 2021, 2019, 2017, 2020, 2018, 2021, 2020],
    'Brand': ['toyota', 'honda', 'ford', 'bmw', 'mercedes', 'toyota', 'honda', 'ford', 'bmw', 'mercedes'],
    'Mileage': [45000, 35000, 25000, 15000, 30000, 55000, 28000, 40000, 18000, 22000],
    'Price': [18500, 17800, 16500, 35000, 32000, 15500, 22000, 25000, 42000, 38000]
})

# Encode categorical variables
le = LabelEncoder()
data['Brand_encoded'] = le.fit_transform(data['Brand'])

# Prepare features and target
X = data[['Year', 'Brand_encoded', 'Mileage']]
y = data['Price']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model and encoder
with open('model.pkl', 'wb') as f:
    pickle.dump((model, le), f)