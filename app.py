import streamlit as st
import pickle

with open('logreg_with_scaler (1).pkl', 'rb') as file:
    model, scaler = pickle.load(file)

st.title("Placement Prediction")

cgpa = st.number_input("Enter CGPA (0.0 - 10.0):", value=6.0, step=0.1)
iq = st.number_input("Enter IQ (50 - 200):", value=100, step=1)

if st.button("Predict!"):
    if not (0.0 <= cgpa <= 10.0):
        st.error("CGPA must be between 0.0 and 10.0.")
    elif not (50 <= iq <= 200):
        st.error("IQ must be between 50 and 200.")
    else:
        input_data = [[cgpa, iq]]
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)
        if prediction == 1:
            st.success("You are likely to be placed!")
        else:
            st.warning("You are less likely to be placed.")




