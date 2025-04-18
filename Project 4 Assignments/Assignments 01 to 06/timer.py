import time

def countdown(seconds):
    print(f"⏱️ Countdown starting for {seconds} seconds...")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Print on the same line
        time.sleep(1)
        seconds -= 1

    print("🚀 Time's up! Let's go!")

# Ask user for input
try:
    total_seconds = int(input("Enter time in seconds: "))
    countdown(total_seconds)
except ValueError:
    print("❌ Please enter a valid number!")
