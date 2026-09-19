# 🌸 Iris Species Predictor

A machine learning web app that classifies Iris flowers into three species — Setosa, Versicolor, and Virginica based on their sepal and petal measurements.

## 🔗 Live Demo
[Try it here](https://iris-app-ann-predictor.streamlit.app)

## 📌 About the Project
This project uses an Artificial Neural Network (ANN) built with TensorFlow/Keras to classify Iris flowers. The model takes four inputs — sepal length, sepal width, petal length, and petal width — and predicts the most likely species.

 🛠️ Tech Stack
Python
TensorFlow / Keras  for building and training the ANN
scikit-learn for data preprocessing (scaling)
Streamlit for the interactive web interface

 How It Works
1. User inputs flower measurements
2. Input is scaled using a pre-fitted `StandardScaler`
3. The trained ANN model predicts the species
4. Result is displayed instantly on the web app

## 📂 Files in this Repo
- `app.py` — Streamlit application code
- `model.keras` — Trained neural network model
- `scaler.pkl` — Fitted scaler for input preprocessing
- `requirements.txt` — Project dependencies

## 👩‍💻 Author
Made by Diya Zahra
