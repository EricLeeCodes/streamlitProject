import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO


# Example CSV Content
csv_content = """Category,Amount,Date
Food,15.50,01-12-2025
Transport,30.00,01-13-2025
Entertainment,25.75,01-14-2025
Food,22.00,01-15-2025
Utilities,60.00,01-16-2025
Transport,10.50,01-17-2025
Entertainment,40.00,01-18-2025
Food,18.25,01-19-2025
"""

# Title and Description
st.markdown("<h1 style='text-align: center; color: #4CAF50'>Personal Expense Tracker</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white ;'>Hello! Upload your expenses to visualize your spending!</h4>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Choose your CSV file", type="csv", label_visibility="collapsed")

# Stylingl for fie uploader and general colors
st.markdown("""
    <style>
        .es2srfl0 {
            width: full;
            font-size: 16px;
            color: #4CAF50;
            font-weight: bold;
            border: 2px solid #4CAF50;
            border-radius: 15px;
            margin-block: 25px;
            background-color: rgb(38, 39, 48);
        }
            
        .e10tffaf0 {
            background-color: black;
        }
            
        .e1w6nwfl0 {
        color: white;
        }
        
            .e1obcldf2 {
            background-color: #262325;
            border-color: #4CAF50}
            

    </style>
""", unsafe_allow_html=True)

# Success message for successful upload
if uploaded_file:
    st.markdown("<p style='padding-top: 15px; text-align: center; color: #4CAF50;'>File Uploaded Successfully!</p>", unsafe_allow_html=True)

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

    st.markdown("<h4 style='padding-block: 25px; color: #4CAF50;'>Your Uploaded CSV Content:</h4>", unsafe_allow_html=True)
    st.write(df) # Displays CSV file
    total_amount = df['Amount'].sum()
    st.markdown(f"<div style='color: white;'>Total Amount Spent: ${total_amount:,.2f}</div>", unsafe_allow_html=True)

    # Bar graph
    bar_fig = px.bar(df, x='Category', y='Amount', title='Total Spending By Category', color='Category')
    st.plotly_chart(bar_fig, key="uploaded_bar_graph")

    # Pie graph
    pie_fig = px.pie(df, names='Category', values='Amount', title='Total Spending By Category', color='Category')
    st.plotly_chart(pie_fig, key="uploaded_pie_chart")

    # Fill in missing values with 0

    if df.isnull().sum().sum() > 0: # First .sum().sum() gives total amount of NaN across data.
        st.warning("Some missing values were found and filled with 0")
        df.fillna(0, inplace=True)


# Example file
example_file = StringIO(csv_content)

st.markdown("<h4 style=' padding-top: 50px; color: #4CAF50;'>Example CSV Content:</h4>", unsafe_allow_html=True)
st.markdown("""
    <style>
        .e12yskxj0 {
            display: flex;
            justify-content: center;
            align-items: center;

        }

        .stDownloadButton {
            display: flex;
            justify-content: center;
            align-items: center;
            color: #4CAF50 !important;
         }
        
        .e1obcldf2:hover  {
            color: #4CAF50;
            border-color: #4CAF50;
        }
            
        .e1obcldf2:focus  {
            color: #4CAF50;
            border-color: #4CAF50;
        }
    
        .e1obcldf2:active {
            color: white;
            border-color: #4CAF50;
            background-color: #4CAF59
        }
        .es2srfl9 {
            color: white;}   
        
    </style>
""", unsafe_allow_html=True)

example_df=pd.read_csv(example_file)
st.write(example_df)
example_total_amount = example_df['Amount'].sum()
st.markdown(f"<div style='color: white'>Total Amount Spent: ${example_total_amount:,.2f}</div>", unsafe_allow_html=True)

# Bar graph
example_bar_fig = px.bar(example_df, x='Category', y='Amount', title='Total Spending By Category', color='Category')
st.plotly_chart(example_bar_fig, key="example_bar_graph")

# Pie graph
example_pie_fig = px.pie(example_df, names='Category', values='Amount', title='Total Spending By Category', color='Category')
st.plotly_chart(example_pie_fig, key="example_pie_chart")

st.markdown("<h5 style='text-align:center; padding-top: 50px; color:white'>You can download this CSV file here to upload yourself!:</h5>", unsafe_allow_html=True)
st.download_button(
    label="Download Example CSV File",
    data=example_file.getvalue(),
    file_name="example_expenses.csv",
    mime="text/csv"
)