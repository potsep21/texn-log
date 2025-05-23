import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans


# Step 3: Algorithm Customization with Sliders
def app3():
    st.title("3. K-Means Clustering with Adjustable K")
    uploaded_file = st.file_uploader("Upload an Iris CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        k = st.slider("Select number of clusters", 2, 10, 3)
        kmeans = KMeans(n_clusters=k, random_state=42)
        df['Cluster'] = kmeans.fit_predict(df.iloc[:, :-1])
        st.write("### Clustering Results:")
        st.dataframe(df)


# Allows running the script independently
if __name__ == "__main__":
    app3()
