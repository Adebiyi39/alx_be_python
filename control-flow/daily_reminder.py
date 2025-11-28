# Prompt for a Single Task

# Ask the user to input a task description
task = input("Enter the task description: ")

# Ask for the task's priority
priority = input("Enter task priority (high, medium, low): ")

# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes or no): ")

# Prompt the Task Based on Priority
match priority.lower():
    case "high":
        reminder = f"The task '{task}' is HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is LOW priority."
    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority."

# Modify the reminder if the task is time-bound
if time_bound.lower() == "yes":
    reminder += " This task requires immediate attention today!"
else:
    reminder += " This task is not time-sensitive."

# Provide a Customizer Reminder
print(reminder)



