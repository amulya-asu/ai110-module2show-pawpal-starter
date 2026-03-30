"""
pawpawl_system.py
Backend classes for the PawPawl pet‑care planner system.
Updated to support multiple pets, pet-specific tasks, recurring tasks,
and lightweight conflict detection.
"""

import datetime

# -------------------------
# Owner
# -------------------------
class Owner:
    """Represents a pet owner who has pets, tasks, and limited daily time."""

    def __init__(self, name, time_available):
        """
        Initialize an Owner.

        name: string, the owner's name
        time_available: int, minutes available per day
        """
        self.name = name
        self.time_available = time_available
        self.pets = []
        self.tasks = []

    def add_pet(self, pet):
        """Add a Pet object to the owner's list of pets."""
        self.pets.append(pet)

    def add_task(self, task):
        """Add a Task object to the owner's list of tasks."""
        self.tasks.append(task)

    def get_info(self):
        """Return a string summarizing the owner's information."""
        return f"Owner: {self.name}, Time Available: {self.time_available} min"


# -------------------------
# Pet
# -------------------------
class Pet:
    """Represents a pet belonging to an owner."""

    def __init__(self, name, species):
        """
        Initialize a Pet.

        name: string, pet's name
        species: string, type of animal
        """
        self.name = name
        self.species = species

    def get_info(self):
        """Return a string summarizing the pet's information."""
        return f"Pet: {self.name} ({self.species})"


# -------------------------
# Task
# -------------------------
class Task:
    """Represents a task related to pet care, with optional recurrence."""

    def __init__(self, name, duration, priority, pet=None, task_time=None, frequency=None, due_date=None):
        """
        Initialize a Task.

        name: string, task name
        duration: int, minutes required
        priority: int, higher means more important
        pet: optional Pet object
        task_time: optional string "HH:MM"
        frequency: "daily", "weekly", or None
        due_date: datetime.date object for recurring tasks
        """
        self.name = name
        self.duration = duration
        self.priority = priority
        self.pet = pet
        self.time = task_time
        self.frequency = frequency
        self.due_date = due_date
        self.completed = False

    def mark_task_complete(self, owner, task):
        """
        Mark a task as complete and generate the next occurrence if recurring.

        owner: Owner object
        task: Task object being completed
        """
        task.completed = True
        next_task = self.create_next_occurrence(task)
        if next_task:
            owner.add_task(next_task)

    def describe(self):
        """Return a readable description of the task."""
        pet_info = f" for {self.pet.name}" if self.pet else ""
        time_info = f" at {self.time}" if self.time else ""
        return f"{self.name}{pet_info}{time_info} — {self.duration} min (priority {self.priority})"


# -------------------------
# Scheduler
# -------------------------
class Scheduler:
    """Handles scheduling, conflict detection, and recurring task generation."""

    def create_next_occurrence(self, task):
        """
        Create the next instance of a recurring task.

        Returns a new Task or None if the task does not recur.
        """
        if not task.frequency:
            return None

        if not task.due_date:
            return None

        if task.frequency == "daily":
            next_date = task.due_date + datetime.timedelta(days=1)
        elif task.frequency == "weekly":
            next_date = task.due_date + datetime.timedelta(weeks=1)
        else:
            return None

        return Task(
            name=task.name,
            duration=task.duration,
            priority=task.priority,
            pet=task.pet,
            task_time=task.time,
            frequency=task.frequency,
            due_date=next_date
        )

    def detect_conflicts(self, tasks):
        """
        Detect tasks scheduled at the same time.

        Returns a list of warning strings instead of raising errors.
        """
        conflicts = []
        time_map = {}

        for task in tasks:
            if task.time:
                time_map.setdefault(task.time, []).append(task)

        for time_slot, task_list in time_map.items():
            if len(task_list) > 1:
                names = ", ".join(t.name for t in task_list)
                conflicts.append(f"⚠️ Conflict at {time_slot}: {names}")

        return conflicts

    def generate_plan(self, owner, tasks=None):
        """
        Generate a daily plan based on priority, time, and available minutes.

        Returns a tuple: (plan, warnings)
        plan: list of Task objects selected
        warnings: list of conflict messages
        """
        tasks = tasks or owner.tasks

        sorted_tasks = sorted(
            tasks,
            key=lambda t: (-t.priority, t.time or "99:99")
        )

        warnings = self.detect_conflicts(sorted_tasks)

        plan = []
        time_left = owner.time_available

        for task in sorted_tasks:
            if task.duration <= time_left:
                plan.append(task)
                time_left -= task.duration

        return plan, warnings

    def explain_plan(self, plan):
        """
        Explain how the plan was generated.

        Returns a string describing the scheduling logic.
        """
        if not plan:
            return "No tasks fit into the available time."

        return (
            "Tasks were selected by choosing the highest priority items first "
            "and fitting as many as possible into the available time. "
            "Tasks may belong to different pets, but all were considered together."
        )