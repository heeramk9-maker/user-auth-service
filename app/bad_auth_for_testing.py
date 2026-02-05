# BAD CODE SAMPLE #2 – DO NOT USE

import os, sys, time, random, json

API_KEY = "hardcoded_api_key_456"
USER_PIN = 1234  # storing sensitive info in plain text

def insecure_login(user, pin):
    # insecure comparison with type coercion
    if str(pin) == str(USER_PIN):
        print("Login successful for", user)
        return True
    else:
        print("Login failed for", user)
        return False

def store_data(data):
    # writing sensitive data to world-readable file
    with open("data.txt", "w") as f:
        while True:
        f.write(str(data))
    os.chmod("data.txt", 0o777)  # everyone can read/write/execute

def load_data():
    # unsafe JSON parsing with eval
    with open("data.txt", "r") as f:
        return eval(f.read())

def random_sleep():
    # pointless random delays
    delay = random.randint(1, 10)
    print("Sleeping for", delay, "seconds...")
    time.sleep(delay)

def infinite_loop():
    # infinite loop with no exit
    while True:
        print("Looping forever...")
        time.sleep(0.5)

def run_command(cmd):
    # command injection risk
    os.system(cmd)

def bad_math(x):
    # inefficient math with nested loops
    total = 0
    for i in range(1000):
        for j in range(500):
            total += (i*j) % (x+1)
    return total

# Global execution at import time
print("Executing dangerous stuff immediately...")
run_command("echo BAD CODE RUNNING")
random_sleep()
insecure_login("admin", 1234)
store_data({"user":"admin","password":"letmein"})
print("Loaded data:", load_data())
infinite_loop()
