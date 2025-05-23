
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans

# Step 6: Sidebar for Settings
def app6():
    st.title("6. Sidebar for Settings")
    st.sidebar.header("Settings")
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data")
        st.dataframe(df)
        k = st.sidebar.slider("Number of Clusters", 2, 10, 3)
        kmeans = KMeans(n_clusters=k, random_state=42)
        df['Cluster'] = kmeans.fit_predict(df.iloc[:, :-1])
        st.write("### Clustering Results")
        st.dataframe(df)

# Allows running the script independently
if __name__ == "__main__":
    app6()