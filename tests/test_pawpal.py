import pytest
from pawpal_system import Owner, Pet, Task
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