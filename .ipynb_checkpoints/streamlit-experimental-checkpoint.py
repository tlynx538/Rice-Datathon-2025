import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import altair as alt


df = pd.read_excel("data/Chevron Challenge Materials/training.xlsx")
st.markdown("# BeliEVe")
st.markdown('Vehicle Inventory for 2025')
# Sample dataframe (replace with your actual data)
# df = pd.read_csv('your_data.csv')  # Example to load your data

# Set a clean and minimalistic style
sns.set(style="ticks")

# Create a larger figure for better readability
plt.figure(figsize=(10, 6))


# Set up the Streamlit app
st.title("Vehicle Data Visualization")

# Display first bar chart: Vehicle Category Distribution
st.subheader("Vehicle Category Distribution")

# Create a dataframe for the 'Vehicle Category' count
vehicle_category_count = df['Vehicle Category'].value_counts().reset_index()
vehicle_category_count.columns = ['Vehicle Category', 'Counts']

# Use Streamlit's native bar chart for Vehicle Category Distribution
st.bar_chart(vehicle_category_count.set_index('Vehicle Category'))

# Display second bar chart: GVWR Class Distribution
st.subheader("GVWR Class Distribution")

# Create a dataframe for the 'GVWR Class' count
gvwr_class_count = df['GVWR Class'].value_counts().reset_index()
gvwr_class_count.columns = ['GVWR Class', 'Counts']

# Use Streamlit's native bar chart for GVWR Class Distribution
st.bar_chart(gvwr_class_count.set_index('GVWR Class'))


