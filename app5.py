import streamlit as st
import pandas as pd
import plotly.express as px

# Step 5: Multi-tab Interface
def app5():
    st.title("5. Multi-tab Interface")
    uploaded_file = st.file_uploader("Upload an Iris CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        tab1, tab2, tab3 = st.tabs(["Dataset", "Statistics", "Plots"])
        with tab1:
            st.write("### Uploaded Data")
            st.dataframe(df)
        with tab2:
            st.write("### Summary Statistics")
            st.write(df.describe())
        with tab3:
            x_axis = st.selectbox("X-axis", df.columns[:-1])
            y_axis = st.selectbox("Y-axis", df.columns[:-1])
            fig = px.scatter(df, x=x_axis, y=y_axis, color=df.columns[-1])
            st.plotly_chart(fig)

# Allows running the script independently
if __name__ == "__main__":
    app5()