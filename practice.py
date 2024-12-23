from datetime import datetime

# Constants for time ranges
MORNING_END = 12
AFTERNOON_END = 16
EVENING_END = 21
NIGHT_END = 23


def get_current_date_and_time():
    """
    Returns the current date and time as a dictionary.
    """
    now = datetime.now()
    return {
        "hour": now.hour,
        "date": now.strftime("%a-%d-%b-%Y"),
        "time": now.strftime("%H:%M:%S"),
    }


def get_greeting(hour):
    """
    Determines the appropriate greeting based on the hour of the day.

    Args:
        hour (int): Current hour (24-hour format).

    Returns:
        str: Greeting message.
    """
    if 0 <= hour < MORNING_END:
        return "morning"
    elif MORNING_END <= hour < AFTERNOON_END:
        return "afternoon"
    elif AFTERNOON_END <= hour <= EVENING_END:
        return "evening"
    elif EVENING_END <= hour <= NIGHT_END:
        return "night"
    else:
        return "Hello"  # Fallback for unexpected cases


def main():
    """
    Main function to execute the greeting logic.
    """
    # Get current date and time details
    current_details = get_current_date_and_time()
    hour = current_details["hour"]
    current_date = current_details["date"]
    current_time = current_details["time"]

    # Get the user's name
    name = input("Enter your name: ").strip()
    if not name:  # Validate input
        print("Name cannot be empty. Please restart the program.")
        return

    # Generate and print the greeting
    greeting = get_greeting(hour)
    print(
        f"Good {greeting}, {name}! The day today is {current_date}, "
        f"and the current time is {current_time}."
    )


if __name__ == "__main__":
    main()
