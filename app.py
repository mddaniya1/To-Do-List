import streamlit as st

# Set the page configuration
st.set_page_config(page_title="To-Do List", page_icon="📝", layout="centered")

# Initialize session state to store tasks
if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

# Title of the app
st.title("📝 To-Do List App")

# Input area to add new tasks
task = st.text_input("Add a new task:", placeholder="Type here and press Enter")

if st.button("Add Task"):  # Add button to handle task addition
    if task:  # Add the task to the list if it's not empty
        st.session_state["task_list"].append(task)
        st.query_params["update"] = "true"  # Use the new query_params API for refresh

# Display the list of tasks
st.subheader("Your Tasks:")
if st.session_state["task_list"]:
    for i, task in enumerate(st.session_state["task_list"]):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.write(f"{i + 1}. {task}")
        with col2:
            if st.button("❌", key=f"delete_{i}"):  # Button to delete the task
                st.session_state["task_list"].pop(i)
                st.query_params["update"] = "true"  # Use the new query_params API for refresh
else:
    st.write("You have no tasks. Start adding some!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit.")
