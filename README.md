# 🐾 PawPal+ — Smart Pet‑Care Scheduling Assistant

PawPal+ is a Streamlit app that helps busy pet owners stay consistent with daily pet‑care routines. It organizes tasks, considers constraints like time and priority, and generates a clear, realistic daily plan. The system supports multiple pets, recurring tasks, conflict detection, and human‑readable explanations.

---

## 🚀 Features

### **Smart Scheduling**
- Sorts tasks by priority first, then by time of day  
- Selects tasks that fit within the owner’s available minutes  
- Produces a realistic, easy‑to‑follow daily plan  

### **Conflict Warnings**
- Detects tasks scheduled at the same time  
- Returns warnings without blocking scheduling  
- Helps users adjust their routines without breaking the plan  

### **Recurring Tasks**
- Supports daily and weekly recurrence  
- Automatically generates the next occurrence when a task is completed  
- Keeps long‑term routines consistent (feeding, medication, etc.)  

### **Multi‑Pet Support**
- Owners can register multiple pets  
- Tasks can be linked to specific animals  
- The scheduler considers all tasks together while preserving pet context  

### **Task Management**
- Add, edit, and describe tasks  
- Track completion status  
- View readable summaries including pet name, time, duration, and priority  

### **Plan Explanation**
- The scheduler includes a built‑in explanation of how the plan was created  
- Helps users understand why certain tasks were chosen or skipped  

---

## 🧠 Smarter Scheduling Logic

PawPal+ uses a simple but effective algorithm:

- Sort tasks by priority, then by time  
- Detect conflicts between tasks with the same time  
- Select tasks that fit within the owner’s available minutes  
- Return both the plan and any warnings  

This keeps the system predictable, safe, and easy to understand while still supporting advanced features like recurrence and multi‑pet scheduling.

---

## 🧪 Testing PawPal+

Run the full test suite:

```bash
python -m pytest
