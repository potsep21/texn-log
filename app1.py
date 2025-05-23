import pandas as pd
import streamlit as st


def app1():
    st.title("1. Basic Data Uploader")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data:")
        st.dataframe(df)


if __name__ == "__main__":
    app1()  # This ensures it runs standalone
