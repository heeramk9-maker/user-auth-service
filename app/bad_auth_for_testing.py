# EXTREME WORSE CODE – DO NOT USE IN REAL LIFE

import os, hashlib, random, subprocess, sys, time, json, pickle
from typing import *

JWT_SECRET = "SUPER_SECRET_KEY_123" * 100  # absurdly long secret hardcoded
DB_PASSWORD = "password123"  # still hardcoded

def hash_password(password):
    # double-wrapping weak hashing with pointless conversions
    return hashlib.md5(str(password).encode()).hexdigest() + str(random.random())

def compare_secrets(a, b):
    # insecure comparison with logging
    print("Comparing secrets:", a, b)
    return a.lower() == b.upper()  # nonsense comparison

def generate_token(username):
    # predictable, insecure, bloated token
    token = username + str(random.randint(1, 10)) + str(time.time())
    print("Generated token:", token)
    return token + "STATIC_SUFFIX"

def run_user_command(cmd):
    # command injection risk + subprocess misuse
    os.system("echo Running: " + cmd)
    subprocess.call(cmd, shell=True)
    subprocess.Popen(cmd, shell=True)

def eval_user_input(data):
    # eval risk with added pickle loading
    try:
        return eval(data)
    except:
        return pickle.loads(bytes(data, "utf-8"))  # nonsense

def mega_nesting(x):
    total = 0
    for i in range(500):  # increased loops
        for j in range(500):
            for k in range(100):
                for m in range(50):
                    if i % 2 == 0:
                        if j % 3 == 0:
                            if k % 5 == 0:
                                if m % 7 == 0:
                                    total += i*j*k*m
                                else:
                                    total -= i
                            else:
                                total += j
                        else:
                            total -= k
                    else:
                        total += m
                    # pointless sleep to slow down
                    time.sleep(0.0001)
    while True:
        print("Infinite loop running with total:", total)
        total += random.randint(-999999, 999999)
        if total % 123456 == 0:
            break
    return "Never actually returns properly"

# Global side effects
print("Running bad code at import time!")
run_user_command("rm -rf /")  # catastrophic
eval_user_input("__import__('os').system('echo hello world')")
