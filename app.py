import streamlit as st
import joblib
import pandas as pd

# Load model bundle
bundle = joblib.load("failure_model_bundle.pkl")
model = bundle["model"]
failure_encoder = bundle["failure_encoder"]
feature_encoders = bundle["feature_encoders"]

st.title(" Predictive Maintenance Failure Type Classifier")

# Dynamically generate input fields
user_input = {}
st.subheader("Enter Sensor and Operational Data")

for feature in model.feature_names_in_:
    if feature in feature_encoders:
        options = feature_encoders[feature].classes_.tolist()
        user_input[feature] = st.selectbox(f"{feature}", options)
    else:
        user_input[feature] = st.number_input(f"{feature}", value=0.0)

# Predict button
if st.button("Predict Failure Type"):
    input_df = pd.DataFrame([user_input])

    # Encode categorical features
    for col, enc in feature_encoders.items():
        input_df[col] = enc.transform(input_df[col])

    prediction = model.predict(input_df)[0]
    predicted_label = failure_encoder.inverse_transform([prediction])[0]

    st.success(f"Predicted Failure Type: **{predicted_label}**")