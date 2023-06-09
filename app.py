import streamlit as st
import pandas as pd
import numpy as np
# from db_fxns import (add_data, view_all_data, view_unique_tasks, 
#                      get_task, edit_task_data)
from db_fxns import *
import plotly.express as px
import datetime


st.title("ToDo App with Streamlit")

menu = ["Create", "Read", "Update", "Delete", "About"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create":
    st.subheader("Add Items")

    col1, col2 = st.columns(2)
    with col1:
        task = st.text_area("Task To Do")
    with col2:
        task_status = st.selectbox("Status", ["To Do", "Doing", "Done"])
        task_due_date = st.date_input("Due date")
    
    if st.button("Add Task"):
        add_data(task, task_status, task_due_date)
        st.success("Successfully Added Task: {}".format(task))

elif choice == "Read":
    st.subheader("Views Items")
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=["Task", "Status", "Due Date"])
    with st.expander("View All Data"):
        st.dataframe(df)

    with st.expander("Task Satus"):
        task_df = df["Status"].value_counts()
        task_df = task_df.reset_index()
        st.dataframe(task_df)

        fig = px.pie(task_df, names="Status", values="count")
        st.plotly_chart(fig)

elif choice == "Update":
    st.subheader("Update/Edit Items")
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=["Task", "Status", "Due Date"])
    with st.expander("Current Data"):
        st.dataframe(df)

    view_unique_task = view_unique_tasks()
    # df_unique = pd.DataFrame(view_unique_task)
    # st.write(view_unique_task)
    lst_of_task = [i[0] for i in view_unique_task]
    # st.write(lst_of_task)

    selected_task = st.selectbox("Select Task To Edit:", lst_of_task)

    selected_result = get_task(selected_task)
    # st.write(selected_result)

    col1, col2 = st.columns(2)
    if selected_result:
        task = selected_result[0][0]
        task_status = selected_result[0][1]
        task_due_date = selected_result[0][2]

        col1, col2 = st.columns(2)
        with col1:
            new_task = st.text_area("Task To Do", task)
        with col2:
            new_task_status = st.selectbox(task_status, ["To Do", "Doing", "Done"])
            new_task_due_date = st.date_input(task_due_date)
        
        if st.button("Update Task"):
            edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
            st.success(f"Successfully Updated:: {task} to :: {new_task}")
    

    result2 = view_all_data()
    # st.write(result)
    df2 = pd.DataFrame(result2, columns=["Task", "Status", "Due Date"])
    with st.expander("Updated Data"):
        st.dataframe(df2)

elif choice == "Delete":
    st.subheader("Delete Items")
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=["Task", "Status", "Due Date"])
    with st.expander("Current Data"):
        st.dataframe(df)


    st.subheader("Update/Edit Items")
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=["Task", "Status", "Due Date"])
    # with st.expander("Current Data"):
    #     st.dataframe(df)

    view_unique_task = view_unique_tasks()
    # df_unique = pd.DataFrame(view_unique_task)
    # st.write(view_unique_task)
    lst_of_task = [i[0] for i in view_unique_task]
    # st.write(lst_of_task)

    selected_task = st.selectbox("Select Task To Delete:", lst_of_task)
    st.warning(f"Do you want to delete {selected_task}")
    if st.button("Delete"):
        delete_task(selected_task)
        st.success("The task has been successfully deleted")

    new_result = view_all_data()
    # st.write(result)
    df3 = pd.DataFrame(new_result, columns=["Task", "Status", "Due Date"])
    with st.expander("Updated Data"):
        st.dataframe(df3)

        

