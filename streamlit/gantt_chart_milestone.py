import streamlit as st
import plotly.figure_factory as ff
import pandas as pd

# Define the main content
st.header("Project Planner")

# Define the input fields for the projects, tasks, and milestones
project_name = st.text_input("Project Name")
task_name = st.text_input("Task Name")
milestone_name = st.text_input("Milestone Name")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# Define the button to add tasks and milestones to the project
if st.button("Add Task"):
    # Load the existing project data from a CSV file
    try:
        df = pd.read_csv(project_name + ".csv")
    except:
        df = pd.DataFrame(columns=["Task", "Milestone", "Start", "Finish"])

    # Add the new task and milestone to the DataFrame
    new_row = {"Task": task_name, "Milestone": milestone_name, "Start": start_date, "Finish": end_date}
    df = df.append(new_row, ignore_index=True)

    # Save the updated DataFrame to a CSV file
    df.to_csv(project_name + ".csv", index=False)

# Define the button to create the timeline chart
if st.button("Create Timeline"):
    # Load the project data from the CSV file
    try:
        df = pd.read_csv(project_name + ".csv")
    except:
        st.error("Project not found")
        st.stop()

    # Convert the DataFrame to a list of dictionaries
    tasks = []
    for i, row in df.iterrows():
        tasks.append(dict(Task=row["Task"], Start=row["Start"], Finish=row["Finish"], Milestone=row["Milestone"]))

    # Create the timeline chart using Plotly
    fig = ff.create_gantt(tasks, colors=["#7B0F00", "#FF5733"], index_col="Milestone", show_colorbar=False, group_tasks=True)
    fig.update_layout(width=800, height=500)

    # Display the chart in the Streamlit app
    st.plotly_chart(fig)