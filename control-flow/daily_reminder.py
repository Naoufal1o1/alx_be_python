# daily_reminder.py

def daily_reminder():
    # Prompt for task and related info
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match-case for priority level
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            return

    # Add time-sensitive message if applicable
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message = "Note: " + message + ". Consider completing it when you have free time."

    # Print the final reminder
    print("\nReminder:", message)

# Run the program
if __name__ == "__main__":
    daily_reminder()
