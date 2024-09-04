import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Create a connection to the SQLite database
engine = create_engine('sqlite:///news.db')

# Read the table 'summarized_news' into a DataFrame
df = pd.read_sql('SELECT * FROM summarized_news', engine)

# Set the title of the Streamlit app
st.title("Sharenews24 Summarized News")

# Display the original news articles
st.subheader("Original News Articles")
st.write(df[['Title', 'Date', 'Description', 'Link']])

# Display the summarized news articles
st.subheader("Summarized News Articles")
st.write(df[['Title', 'Date', 'Summary', 'Link']])

# Filter news articles by date
date_filter = st.text_input('Filter by Date (YYYY-MM-DD):', '')
if date_filter:
    # Apply date filter to the DataFrame
    filtered_df = df[df['Date'].str.contains(date_filter)]
    st.subheader(f"News from {date_filter}")
    st.write(filtered_df[['Title', 'Summary', 'Link']])

