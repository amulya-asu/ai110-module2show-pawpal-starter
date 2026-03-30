import pytest
from pawpal_system import Owner, Pet, Task, Scheduler
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
def test_add_task_to_owner():
    owner = Owner("Alex", 60)
    pet = Pet("Luna", "Dog")
    owner.add_pet(pet)

    assert len(owner.tasks) == 0

    task = Task("Walk", 30, 5, pet=pet)
    owner.add_task(task)

    assert len(owner.tasks) == 1
    assert owner.tasks[0].pet is pet
def test_task_completion():
    task = Task("Walk", 30, 5)
    assert task.completed is False

    task.mark_complete()

    assert task.completed is True
def test_sorting_correctness():
    owner = Owner("Alex", 200)
    pet = Pet("Jack", "dog")

    t1 = Task("Morning Walk", 20, 2, pet, task_time="08:00")
    t2 = Task("Breakfast", 10, 2, pet, task_time="07:30")
    t3 = Task("Playtime", 15, 2, pet, task_time="09:00")

    owner.add_task(t1)
    owner.add_task(t2)
    owner.add_task(t3)

    scheduler = Scheduler()
    plan, warnings = scheduler.generate_plan(owner)

    assert plan[0].time == "07:30"
    assert plan[1].time == "08:00"
    assert plan[2].time == "09:00"

    print("Sorting Correctness Test Passed")
def test_recurrence_logic():
    owner = Owner("Alex", 200)
    pet = Pet("Jack", "dog")

    today = datetime.date.today()
    task = Task("Feed Jack", 10, 3, pet, task_time="07:30",
                frequency="daily", due_date=today)

    owner.add_task(task)

    scheduler = Scheduler()

    # Mark the task complete
    next_task = scheduler.create_next_occurrence(task)

    assert next_task is not None
    assert next_task.due_date == today + datetime.timedelta(days=1)
    assert next_task.name == "Feed Jack"

    print("Recurrence Logic Test Passed")
def test_conflict_detection():
    owner = Owner("Alex", 200)
    pet1 = Pet("Jack", "dog")
    pet2 = Pet("Canes", "dog")

    t1 = Task("Walk Jack", 20, 2, pet1, task_time="08:00")
    t2 = Task("Walk Canes", 20, 2, pet2, task_time="08:00")

    owner.add_task(t1)
    owner.add_task(t2)

    scheduler = Scheduler()
    plan, warnings = scheduler.generate_plan(owner)

    assert len(warnings) == 1
    assert "08:00" in warnings[0]
    assert "Walk Jack" in warnings[0]
    assert "Walk Canes" in warnings[0]

    print("Conflict Detection Test Passed")