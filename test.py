import time
import keyboard

# Function to perform a procedure
def perform_procedure(start=0):
    for i in range(start, 10):
        print(f"Processing step {i}")
        time.sleep(1)  # Simulate a time-consuming task
        
        # Check for a specific keyboard command (e.g., 's' key)
        if keyboard.is_pressed('s'):
            print("\nCommand 's' received! Pausing and saving progress...")
            return i  # Return the current progress
    return None

# Main loop
progress = 0  # Variable to track progress
while progress is not None:
    progress = perform_procedure(progress + 1)
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxsssssssssssssssssssssssssss