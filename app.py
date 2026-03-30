import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")


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
time_available = st.number_input("Available time (minutes)", min_value=0, max_value=1440, value=120)

if st.button("Save Owner"):
    st.session_state.owner = Owner(owner_name, time_available)
    st.success("Owner saved!")

owner = st.session_state.owner

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet"):
    if owner is None:
        st.error("Please save the owner first.")
    else:
        pet = Pet(pet_name, species)
        owner.add_pet(pet)
        st.session_state.pets.append(pet)
        st.success(f"{pet.name} added to {owner.name}.")

if st.session_state.pets:
    st.write("Current pets:")
    st.table(
        [
            {
                "Pet": pet.name,
                "Species": pet.species,
            }
            for pet in st.session_state.pets
        ]
    )
else:
    st.info("No pets yet. Add one above.")

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

task_time = st.text_input("Task time (optional, HH:MM)", value="", placeholder="07:30")

if st.session_state.pets:
    selected_pet = st.selectbox(
        "Assign to pet",
        options=st.session_state.pets,
        format_func=lambda pet: f"{pet.name} ({pet.species})",
    )
else:
    selected_pet = None
    st.caption("Add a pet first to assign tasks to a specific pet.")

if st.button("Add task"):
    priority_map = {"low": 1, "medium": 2, "high": 3}
    cleaned_time = task_time.strip() or None
    new_task = Task(
        task_title,
        duration,
        priority_map[priority],
        pet=selected_pet,
        task_time=cleaned_time,
    )
    st.session_state.tasks.append(new_task)
    st.success("Task added!")

if st.session_state.tasks:
    st.write("Current tasks:")
    task_rows = []
    for t in st.session_state.tasks:
        task_rows.append(
            {
                "Task": t.name,
                "Duration (min)": t.duration,
                "Priority": t.priority,
                "Time": t.time or "Unscheduled",
                "Pet": t.pet.name if t.pet else "None",
                "Completed": t.completed,
            }
        )

    st.table(task_rows)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
if st.button("Generate schedule"):
    if st.session_state.owner is None:
        st.error("Please create an owner first.")
    else:
        owner = st.session_state.owner
        real_tasks = st.session_state.tasks

        scheduler = Scheduler()
        plan, warnings = scheduler.generate_plan(owner, real_tasks)

        st.subheader("Today's Schedule")

        if warnings:
            st.error(
                "Conflict detected. This schedule is not possible as-is until the overlapping tasks are adjusted."
            )
            for warning in warnings:
                st.write(warning)

        if not plan:
            st.warning("No tasks fit into the available time.")
        else:
            plan_rows = []
            for task in plan:
                plan_rows.append(
                    {
                        "Task": task.name,
                        "Time": task.time or "Unscheduled",
                        "Duration (min)": task.duration,
                        "Priority": task.priority,
                        "Pet": task.pet.name if task.pet else "None",
                    }
                )

            st.success(f"{len(plan_rows)} task(s) scheduled successfully.")
            st.table(plan_rows)

            unscheduled_tasks = [task for task in real_tasks if task not in plan]
            if unscheduled_tasks:
                st.caption("Tasks that did not fit into the available time:")
                st.table(
                    [
                        {
                            "Task": task.name,
                            "Time": task.time or "Unscheduled",
                            "Duration (min)": task.duration,
                            "Priority": task.priority,
                            "Pet": task.pet.name if task.pet else "None",
                        }
                        for task in unscheduled_tasks
                    ]
                )

            st.info(scheduler.explain_plan(plan))
