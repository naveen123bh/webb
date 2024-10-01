import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt  # Importing matplotlib for plotting

# Title and subheader
st.title("Data Analysis")
st.subheader("Data analysis using Python")

# File uploader for CSV
upload = st.file_uploader("Upload your dataset (in CSV format)")
if upload is not None:
    # Read the CSV file with low_memory set to False
    data = pd.read_csv(upload, low_memory=False)

    # Check for null values
    null_values = data.isnull().sum()
    if st.checkbox("Show Null Values Count"):
        st.write("Null Values in Each Column:")
        st.write(null_values[null_values > 0])  # Display only columns with null values

    # Preview Dataset
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

    # Display data types of columns
    if st.checkbox("Datatype of Each Column"):
        st.text("Datatypes")
        st.write(data.dtypes)

    # Checking the number of rows or columns
    dimension = st.radio("Which dimension do you want to check?", ('Rows', 'Columns'))
    if dimension == 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    elif dimension == 'Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])

    # Check for null values and display heatmap
    if data.isnull().values.any():
        if st.checkbox('Show Null Values Heatmap'):
            plt.figure(figsize=(10, 6))  # Set the figure size
            sns.heatmap(data.isnull(), cbar=False, cmap='viridis')  # Create a heatmap for null values
            st.pyplot()  # Render the heatmap in the Streamlit app

    # Check for duplicates
    test = data.duplicated().any()  # Check for duplicates
    if test:  # If there are duplicates
        st.warning("Dataset contains duplicates.")
        dup = st.selectbox("Do you want to remove duplicates?", ("select one", "yes", "no"))

        # Handle the user's selection
        if dup == "yes":
            data = data.drop_duplicates()  # Remove duplicates
            st.text("Duplicate values removed now.")
        elif dup == "no":
            st.text("Ok, no problem.")

    # Display summary of the dataset
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include='all'))
