import streamlit as st
import numpy as np
import joblib
from tensorflow import keras

model = keras.models.load_model('model.keras')
scaler = joblib.load('scaler.pkl')

st.title("Iris Species Predictor")

sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    species = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"Predicted Species: {species[np.argmax(prediction)]}")
