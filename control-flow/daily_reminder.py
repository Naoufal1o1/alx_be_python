# daily_reminder.py

def daily_reminder():
    # Prompt for task and related info
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match-case for priority level
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            return

    # Construct final message
    if time_bound == "yes":
        print(f"Reminder: {base_message} that requires immediate attention today!")
    else:
        print(f"Reminder: Note: {base_message}. Consider completing it when you have free time.")

# Run the program
if __name__ == "__main__":
    daily_reminder()
