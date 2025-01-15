import streamlit as st

st.title("Personal Expense Tracker")

st.write("Hello! Upload your expenses to visualize your spending!")
st.write("Please upload a CSV file with columns: 'Category', 'Amount', 'Date'.")

uploaded_file = st.file_uploader("Choose your CSV file", type="csv")

if uploaded_file:
    st.write("File uploaded successfully!")