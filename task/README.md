# Hands-on task

This task is designed for a Git workshop where multiple teams work on the same section of code. Each team must replace an identical placeholder block in `task.py` with an if condition that adds your team’s greeting. 

The purpose of the task is to (re-)create a realistic flow in development, including merge conflicts and pull requests.

## Scenario

In `tasks.py`, you will find a **TEAM GREETING BLOCK** that looks like this:

```python
# >>>>>>>> TEAM GREETING BLOCK - REPLACE THE NEXT LINES WITH YOUR IF CONDITION <<<<<<<<<<
message += " DEFAULT GREETING!"  # Replace this line
# <<<<<<<<<< END TEAM GREETING BLOCK >>>>>>>>>>
```

Your Task:
Replace this entire block with your team’s if condition. For example:

- Team Alpha:

```python

if user_team == "Alpha":
message += " Greetings from Team Alpha!"

```

- Team Beta:

```python

if user_team == "Beta":
message += " Greetings from Team Beta!"

```

- Team Gamma:

```python

if user_team == "Gamma":
message += " Greetings from Team Gamma!"

```

Because every team edits the exact same block, merging branches will produce merge conflicts that must be manually resolved. In the final, merged version, the block should contain all team-specific if conditions.
