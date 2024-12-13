import streamlit as st
import pickle

with open('logreg_with_scaler (1).pkl', 'rb') as file:
    model, scaler = pickle.load(file)  

st.title("Placement Prediction")

cgpa = st.number_input("Enter CGPA:", min_value=0.0, max_value=10.0, value=6.0)
iq = st.number_input("Enter IQ:", min_value=50, max_value=200, value=100)

input_data = [[cgpa, iq]]
input_data_scaled = scaler.transform(input_data)  

if st.button('Predict'):

    prediction = model.predict(input_data_scaled)
    if prediction == 1:
        st.write("You are likely to be placed!")
    else:
        st.write("You are less likely to be placed.")
