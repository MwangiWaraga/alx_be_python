
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a {priority} priority and its not time bound, you can finish by the end of tomorrow. ")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority and time bound, finish it before the close of the day ")
        else:
            print(f"'{task}' is a {priority} priority and not time bound. You can look at it tomorrow. ")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority and timebound. Finish it after you have cleared all your today tasks")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

