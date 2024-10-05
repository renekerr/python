import sys
import time
import threading

# List of symbols for the animation
symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']

# Flag to stop the animation
stop_animation = False


# Function to display the waiting animation
def waiting_animation():
    global stop_animation
    while not stop_animation:
        for symbol in symbols:
            if stop_animation:
                break
            sys.stdout.write('\r' + symbol)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r')  # Clear the animation when done


# Function to load data from a file (simulated with sleep)
def load_data():
    time.sleep(5)  # Simulate a delay in loading data
    return "Data loaded"


# Start the animation in a separate thread
animation_thread = threading.Thread(target=waiting_animation)
animation_thread.start()

# Load the data
data = load_data()

# Stop the animation
stop_animation = True
animation_thread.join()

# Print the result
print("Data loading completed.")
print(data)
