import streamlit as st

st.markdown("<h1 style='text-align: center; color: #4CAF50'>Personal Expense Tracker</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: white ;'>Hello! Upload your expenses to visualize your spending!</h4>", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Choose your CSV file", type="csv", label_visibility="collapsed")

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

if uploaded_file:
    st.write("File uploaded successfully!")