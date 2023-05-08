import streamlit as st
import plotly.figure_factory as ff
import pandas as pd

# Define the main content
st.header("Gantt Chart")

# Define the input field for the data
data_input = st.text_area("Enter Data (CSV)")

# Define the button to create the chart
if st.button("Create Chart"):
    # Convert the input data to a pandas DataFrame
    df = pd.read_csv(data_input)

    # Convert the DataFrame to a list of dictionaries
    tasks = []
    for i, row in df.iterrows():
        tasks.append(dict(Task=row["Task"], Start=row["Start"], Finish=row["Finish"]))

    # Create the Gantt Chart using Plotly
    fig = ff.create_gantt(tasks, colors=["#7B0F00", "#FF5733"], index_col="Task", show_colorbar=False)
    fig.update_layout(width=800, height=500)

    # Display the chart in the Streamlit app
    st.plotly_chart(fig)