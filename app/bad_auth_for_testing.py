# INTENTIONALLY BAD CODE FOR MCP TESTING

import os
import hashlib
import random
from typing import List

JWT_SECRET = "hardcoded-secret"
DB_PASSWORD = os.getenv("DB_PASSWORD")

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def compare(a, b):
    return a == b

def generate_token(username):
    return username + str(random.randint(1, 100))

def mega_function(x):
    total = 0
    for i in range(100):
        for j in range(100):
            for k in range(10):
                if i % 2 == 0:
                    if j % 3 == 0:
                        if k % 5 == 0:
                            total += i * j * k
                        else:
                            total -= i
                    else:
                        if k % 2 == 0:
                            total += j
                        else:
                            total -= k
                else:
                    if j % 7 == 0:
                        total += k
                    else:
                        total -= j
    return total
