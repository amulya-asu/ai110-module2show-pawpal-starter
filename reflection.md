# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- The scheduler considers priority first so that essential pet‑care tasks are handled before anything optional.
- It also checks the owner's available time and only includes tasks that fit within the daily time limit.
- How did you decide which constraints mattered most?
- If a task has a specific time of day, the scheduler uses that to order tasks and detect conflicts.


**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
    - The scheduler chooses higher‑priority tasks even if lower‑priority tasks might allow more total tasks to fit in the schedule.
    - It does not attempt to optimize for maximum task count because safety and essential care matter more than efficiency.
    - This tradeoff is reasonable because missing a high‑priority task like feeding or medication is more harmful than skipping a lower‑priority activity.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- I used AI mainly to refine ideas I had already brainstormed. Instead of asking it to invent the whole design, I wrote out my thoughts in sentences and asked it to help shape them into cleaner logic.
- When writing code, I avoided having the AI generate full solutions from scratch. I commented what each part should do, then asked the AI to fill in the logic inside those comments. This kept the structure mine while still getting help with details.
- I used AI for debugging and refactoring. When something broke or felt messy, I asked for explanations or simpler alternatives, then tested the suggestions with my own examples to verify they worked.

- What kinds of prompts or questions were most helpful?
- Prompts where I described the behavior I wanted in plain English and asked the AI to turn that into code were the most effective.
- Asking for small, focused improvements like “simplify this method” or “why is this error happening” gave clearer results than asking for full rewrites.


**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
  -- I avoided suggestions that tried to use an LLM to generate summaries or outputs inside the program. When the AI drifted into that direction, I rejected the idea and kept the logic grounded in normal Python code.
- How did you evaluate or verify what the AI suggested?
    - Tested with an example where I first stimulated owner's schedule and inserted a new task to see if the AI's logic for handling that case worked as expected.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested adding different pets to an owner, creating tasks for each pet, and checking whether the scheduler handled conflicting times correctly. I also tested task completion and whether recurring tasks generated the next day’s task properly. 
- Why were these tests important?
These tests were important because they showed whether the schedule generator behaved the way I expected and whether the core logic held up under common scenarios. Without these tests, it would have been hard to trust that the system was making reasonable decisions.
**b. Confidence**

- How confident are you that your scheduler works correctly?
I would say I’m around an 8 out of 10 in confidence that the scheduler works correctly. The main logic feels solid, and the tests covered the most important behaviors. 
- What edge cases would you test next if you had more time?
If I had more time, I would test matching or merging similar tasks across pets to avoid duplicates and see if the system could group related actions more intelligently.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I’m most satisfied with how clearly I understood the logic before writing the code. That made it easier to trace what was happening and write tests that actually caught issues. Once the structure was in place, adding features like recurrence and conflict detection felt pretty natural.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would try to reduce repeated logic and maybe store more data so the system could track habits over time. I’d also explore merging similar tasks so the schedule feels cleaner and less repetitive. There’s room to make the scheduler smarter without making it overly complicated
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One big thing I learned is how important OOP structure is when building a system like this. While writing the tests, I ran into import errors, and adding the __init__.py file (suggested by Copilot) helped me understand how Python packages actually work. It made me realize that small structural details can save a lot of debugging time.
AI Strategy Reflection
Which Copilot features were most effective?
The inline suggestions in VS Code were the most helpful because they sped up writing repetitive parts of the classes and tests. Copilot was especially good at filling in method stubs and reminding me of patterns I had already used. It felt like having a second pair of eyes that kept the code consistent.
One AI suggestion you rejected or modified
At one point Copilot suggested combining multiple responsibilities into a single method in the Scheduler, but I changed it because it made the design messy. I preferred keeping conflict detection, recurrence, and plan generation separate so the system stayed readable. It reminded me that AI can be helpful, but I still need to guide the architecture.
How separate chat sessions helped
Using separate chat sessions for each phase kept me organized and prevented the conversation from getting cluttered. It helped me focus on design first, then implementation, then testing, instead of mixing everything together. It also made it easier to go back and review decisions from earlier phases.
What you learned about being the “lead architect” with AI tools
I learned that working with AI is most effective when I stay in control of the structure and let the AI help with the details. Copilot can generate a lot of ideas, but it’s up to me to decide what fits the system and what doesn’t.
