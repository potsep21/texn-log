import pandas as pd
import streamlit as st
import joblib

def app9():
    st.title("9. Upload Test Data & Predict")

    uploaded_model = st.file_uploader("Upload Trained Model", type=["pkl"])
    uploaded_test = st.file_uploader("Upload Test CSV", type=["csv"])

    if uploaded_model and uploaded_test:
        # Load trained model
        model = joblib.load(uploaded_model)

        # Load test dataset
        test_data = pd.read_csv(uploaded_test)

        # Identify the correct features used during training
        expected_features = model.feature_names_in_

        # Drop any extra columns that were not used during training
        test_data_filtered = test_data[expected_features]

        # Make predictions
        predictions = model.predict(test_data_filtered)

        # Add predictions to the dataframe
        test_data["Predicted Class"] = predictions

        # Display results
        st.write("### Predictions")
        st.dataframe(test_data)

# Allows running the script independently
if __name__ == "__main__":
    app9()
