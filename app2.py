import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans

def app2():
    st.title("2. Data Uploader + K-Means Clustering")
    
    uploaded_file = st.file_uploader("Upload an Iris CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data:")
        st.dataframe(df)
        
        # Perform K-Means clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        df['Cluster'] = kmeans.fit_predict(df.iloc[:, :-1])
        
        st.write("### Clustering Results:")
        st.dataframe(df)

# Allows running the script independently
if __name__ == "__main__":
    app2()
