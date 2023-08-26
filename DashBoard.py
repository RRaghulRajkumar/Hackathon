import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.title("Farmer Dashboard")

# Simulated farmer data
farmer_data = pd.DataFrame({
    'Name': ['Farmer 1', 'Farmer 2', 'Farmer 3', 'Farmer 4', 'Farmer 5'],
    'Crop': ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Mangoes'],
    'Revenue': np.random.randint(1000, 5000, size=5),
    'Expenses': np.random.randint(500, 2000, size=5)
})

# Display farmer data in a table
st.subheader("Farmer Data")
st.dataframe(farmer_data)

# Visualization - Bar chart
st.subheader("Revenue and Expenses Comparison")
st.bar_chart(farmer_data[['Revenue', 'Expenses']], use_container_width=True)
