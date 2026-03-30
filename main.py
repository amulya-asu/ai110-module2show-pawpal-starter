# Importing all classes from pawpal_system.py
import datetime

from pawpal_system import Owner, Pet, Task, Scheduler

# Create an owner and 2 pets
owner = Owner("Alex", 200)
pet1 = Pet("Jack", "dog")
pet2 = Pet("Canes", "dog")

owner.add_pet(pet1)
owner.add_pet(pet2)

# Create tasks (priority: 3 = highest, 1 = lowest)
task1 = Task("Feed Jack", 10, 1, pet1)
task2 = Task("Wash Jack", 30, 2, pet1)
task3 = Task("Play with Jack", 20, 3, pet1)

task4 = Task("Feed Canes", 10, 1, pet2)
task5 = Task("Wash Canes", 30, 2, pet2)
task6 = Task("Play with Canes", 20, 3, pet2)


# Add tasks OUT OF ORDER
owner.add_task(task5)  # priority 2
owner.add_task(task1)  # priority 1
owner.add_task(task3)  # priority 3
owner.add_task(task4)  # priority 1
owner.add_task(task6)  # priority 3
owner.add_task(task2)  # priority 2
task7 = Task("Feed Jack", 10, 1, pet1, task_time="07:30", frequency="daily", due_date=datetime.date.today())
owner.add_task(task7)
# Generate schedule
task8 = Task("Walk Jack", 15, 2, pet1, task_time="08:00")
task9 = Task("Walk Canes", 15, 2, pet2, task_time="08:00")

owner.add_task(task8)
owner.add_task(task9)

scheduler = Scheduler()

plan, warnings = scheduler.generate_plan(owner)

print("Tasks in schedule (sorted by priority):")
for t in plan:
    print(" -", t.describe())

# Print conflict warnings
if warnings:
    print("\nConflict Warnings:")
    for w in warnings:
        print(" ", w)