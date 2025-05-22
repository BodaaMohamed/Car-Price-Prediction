import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load your trained model and columns
model = pickle.load(open('model.pkl', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

st.header('Car Price Prediction ML Model (Notebook Version)')

# Collect user input for each feature
year = st.slider('Year', 1990, 2024, 2015)
engine_hp = st.number_input('Engine HP', min_value=50.0, max_value=1000.0, value=200.0)
engine_cylinders = st.number_input('Engine Cylinders', min_value=2.0, max_value=16.0, value=4.0)
number_of_doors = st.number_input('Number of Doors', min_value=2.0, max_value=6.0, value=4.0)
highway_mpg = st.number_input('Highway MPG', min_value=5, max_value=100, value=30)
city_mpg = st.number_input('City MPG', min_value=5, max_value=100, value=20)
popularity = st.number_input('Popularity', min_value=0, max_value=10000, value=1000)

# For categorical features, use selectbox and then one-hot encode as needed
# Expand to include all possible options as in your training data
make_options = ['BMW', 'Audi', 'Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'Volkswagen', 'Hyundai', 'Kia']  # Example, replace with your full list
transmission_options = ['MANUAL', 'AUTOMATIC', 'AUTOMATED_MANUAL', 'DIRECT_DRIVE', 'UNKNOWN']  # Example, replace with your full list
# Add more categorical fields and their options as needed

make = st.selectbox('Make', make_options)
transmission = st.selectbox('Transmission Type', transmission_options)
# Add more categorical fields as needed

# Prepare the input data for prediction
input_dict = {
    'Year': year,
    'Engine HP': engine_hp,
    'Engine Cylinders': engine_cylinders,
    'Number of Doors': number_of_doors,
    'highway MPG': highway_mpg,
    'city mpg': city_mpg,
    'Popularity': popularity,
}
# One-hot encode all categorical variables to match model_columns
for m in make_options:
    input_dict[f'Make_{m}'] = 1 if make == m else 0
for t in transmission_options:
    input_dict[f'Transmission Type_{t}'] = 1 if transmission == t else 0
# Add similar logic for all other categorical variables used in your model

input_df = pd.DataFrame([input_dict])

# Add missing columns and reorder to match model_columns
for col in model_columns:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[model_columns]

if st.button('Predict'):
    prediction = model.predict(input_df)[0]
    st.success(f'Estimated Car Price: ${prediction:,.2f}')