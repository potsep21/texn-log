import streamlit as st
import pandas as pd

# Step 7: Dynamic Filtering
def app7():
    st.title("7. Dynamic Filtering")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        search_term = st.text_input("Filter Species:")
        filtered_df = df[df[df.columns[-1]].astype(str).str.contains(search_term, case=False, na=False)]
        st.dataframe(filtered_df)

# Allows running the script independently
if __name__ == "__main__":
    app7()