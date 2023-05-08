import streamlit as st
import pandas as pd

# Define the structure of the data
data = pd.DataFrame(columns=["Task", "Project", "Time Spent"])

# Define the sidebar options
projects = st.sidebar.selectbox("Select Project", ["Project 1", "Project 2", "Project 3"])

# Define the main content
st.header("Task Manager")

# Define the input fields
task = st.text_input("Enter Task")
time_spent = st.number_input("Enter Time Spent (in minutes)")

# Define the button to add tasks
if st.button("Add Task"):
    data.loc[len(data)] = [task, projects, time_spent]
    st.success("Task Added")

# Define the button to view tasks
if st.button("View Tasks"):
    st.dataframe(data)
