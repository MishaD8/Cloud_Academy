import random
import time

def simulate_instance_state():
    states = ["crushed", "crushed", "crushed", "running"]
    return random.choice (states)

instance_state = "crushed"
attempts = 0

while instance_state != "running" and attempts < 5:
    print(f"Attempt {attempts + 1}: Instance state is {instance_state}")
    instance_state = simulate_instance_state()
    attempts += 1
    time.sleep(1)           #Wait for 1 second between checks

if instance_state == "running":
    print("Instance is now running!")
else:
    print("Instance did not start in time")


