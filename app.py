import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
# Initialize session state objects
if "owner" not in st.session_state:
    st.session_state.owner = None

if "pets" not in st.session_state:
    st.session_state.pets = []

if "tasks" not in st.session_state:
    st.session_state.tasks = []
st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
# Create owner only once
if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_name, time_available)

owner = st.session_state.owner
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
if st.button("Create Owner & Pet"):
    owner = Owner(owner_name, time_available=120)  # or add a UI field for time
    pet = Pet(pet_name, species)

    owner.add_pet(pet)

    st.session_state.owner = owner
    st.session_state.pets.append(pet)

    st.success("Owner and pet created!")
st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    if st.session_state.pets:
        pet_obj = st.session_state.pets[0]  # simple version: first pet
    else:
        pet_obj = None

    new_task = Task(task_title, duration, priority, pet=pet_obj)
    st.session_state.tasks.append(new_task)

    st.success("Task added!")

if st.session_state.tasks:
    st.write("Current tasks:")
    task_rows = []
    for t in st.session_state.tasks:
        task_rows.append({
            "Task": t.name,
            "Duration (min)": t.duration,
            "Priority": t.priority,
            "Pet": t.pet.name if t.pet else "—",
            "Completed": t.completed
            })

    st.table(task_rows)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
if st.button("Generate schedule"):

    # 1. Ensure owner exists
    if st.session_state.owner is None:
        st.error("Please create an owner and pet first.")
    else:
        owner = st.session_state.owner

        # 2. Use the Task objects directly
        real_tasks = st.session_state.tasks

        # 3. Run the scheduler
        scheduler = Scheduler()
        plan = scheduler.generate_plan(owner, real_tasks)

        # 4. Display results
        st.subheader("Today's Schedule")

        if not plan:
            st.warning("No tasks fit into the available time.")
        else:
            for task in plan:
                st.write("• " + task.describe())

            st.info(scheduler.explain_plan(plan))
