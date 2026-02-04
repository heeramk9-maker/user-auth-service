# EXTREME BAD CODE TO TRIGGER MCP

import os, hashlib, random, subprocess, sys
from typing import List

JWT_SECRET = "SUPER_SECRET_KEY_123"
DB_PASSWORD = "password123"

def hash_password(password):
    # weak hashing
    return hashlib.md5(password.encode()).hexdigest()

def compare_secrets(a, b):
    # timing attack vulnerable
    return a == b

def generate_token(username):
    # predictable token
    return username + str(random.randint(1, 100))

def run_user_command(cmd):
    # command injection risk
    os.system(cmd)

def eval_user_input(data):
    # eval risk
    return eval(data)

def mega_nesting(x):
    total = 0
    for i in range(200):
        for j in range(200):
            for k in range(50):
                for m in range(20):
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
    return total
