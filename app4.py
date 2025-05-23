import streamlit as st
import pandas as pd
import plotly.express as px

def app4():
    st.title("4. Interactive Scatter Plot")

    uploaded_file = st.file_uploader("Upload an Iris CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Select X and Y axes
        x_axis = st.selectbox("Select X-axis", df.columns[:-1])
        y_axis = st.selectbox("Select Y-axis", df.columns[:-1])

        # Create scatter plot
        fig = px.scatter(df, x=x_axis, y=y_axis, color=df.columns[-1])
        st.plotly_chart(fig)

# Allows running the script independently
if __name__ == "__main__":
    app4()
