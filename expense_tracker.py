import streamlit as st
import pandas as pd

# Title and Description
st.markdown("<h1 style='text-align: center; color: #4CAF50'>Personal Expense Tracker</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white ;'>Hello! Upload your expenses to visualize your spending!</h4>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Choose your CSV file", type="csv", label_visibility="collapsed")

# Styling for file uploader
st.markdown("""
    <style>
        .es2srfl0 {
            font-size: 16px;
            color: #4CAF50;
            font-weight: bold;
            border: 2px solid #4CAF50;
            border-radius: 15px;
            margin-block: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# Success message for successful upload
if uploaded_file:
    st.write("File uploaded successfully!")

# Instruction box for CSV formatting
st.markdown("""
    <div style="background-color: rgb(38, 39, 48); padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
        <h4 style="color: #4CAF50;">Instructions:</h4>
        <p style="color: white; font-weight: bold;">Please upload a CSV file with the following columns:</p>
        <ul style="color: white;">
            <li><b>Category</b>: The category of the expense (e.g., Food, Transport)</li>
            <li><b>Amount</b>: The amount spent</li>
            <li><b>Date</b>: The date of the expense (e.g., 01-14-2025)</li>
        </ul>
    </div>
""", unsafe_allow_html=True)


# Pandas logic for reading CSV file

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head()) # Displays first 5 rows
    st.write(df.columns) # Displays column names
    st.write(df.dtypes) # Displays data types of each column
    st.write(df.info()) # Displays basic information    

    # Fill in missing values with 0

    if df.isnull().sum().sum() > 0: # First .sum().sum() gives total amount of NaN across data.
        st.warning("Some missing values were found and filled with 0")
        df.fillna(0, inplace=True)

