
# 🚗 Car Price Prediction App

This repository contains a **Streamlit web application** for predicting used car prices using a machine learning model. The model is trained on various car attributes such as make, transmission type, engine specs, and fuel efficiency.

## 🔍 Overview

The app allows users to input car features such as:
- Year
- Engine HP
- Engine Cylinders
- Number of Doors
- Highway MPG
- City MPG
- Popularity
- Make (e.g., BMW, Audi, Toyota...)
- Transmission Type (e.g., MANUAL, AUTOMATIC...)

Once the user inputs the data, the app uses a **pre-trained machine learning model** to predict the estimated price of the car.

## 🛠 Files

- `app.py`: Main Streamlit app for prediction.
- `model.pkl`: Pickled machine learning model used for prediction.
- `model_columns.pkl`: Pickled list of feature columns used during training to ensure proper data formatting.
- `pre-pare-data.ipynb`: Jupyter Notebook used to preprocess the data and train the model.

## ▶️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/BodaaMohamed/Car-Price-Prediction.git
cd Car-Price-Prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, you can manually install the main dependencies:
```bash
pip install streamlit pandas numpy scikit-learn
```

### 3. Run the app
```bash
streamlit run app.py
```

## 📊 Model Details

The model was trained using car features and one-hot encoded categorical data. It was built and tested in a Jupyter Notebook (`pre-pare-data.ipynb`) and exported using `pickle`.

## 🧠 Features
- Real-time price prediction
- Interactive sliders and dropdowns
- Data preprocessing and model matching



## 📌 Notes
- Be sure the `model.pkl` and `model_columns.pkl` files are in the same directory as `app.py`.
- This is a demo and should not be used for commercial valuations.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
