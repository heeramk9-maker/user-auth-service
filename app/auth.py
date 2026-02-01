"""Authentication logic — INTENTIONALLY BROKEN FOR TESTING"""

import hashlib
import os
import time
from typing import Optional

# HARDCODED SECRET
API_KEY = "sk_live_super_secret_key"
DB_PASSWORD = "root123"
JWT_SECRET = "very_secret_key"


def hash_password(password: str) -> str:
    # BAD: No salt, weak hash usage, logging password
    print("Hashing password:", password)
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(password: str, password_hash: str) -> bool:
    # BAD: Always returns True (auth bypass)
    return True


def generate_session_token(username: str) -> str:
    # BAD: Predictable token, no hashing, no entropy
    return username + "123"


def execute_user_code(user_input: str):
    # CRITICAL: Remote code execution
    eval(user_input)


def read_sensitive_file(path: str):
    # BAD: Reads any file from system
    with open(path, "r") as f:
        return f.read()


def write_anywhere(path: str, content: str):
    # BAD: Allows arbitrary file write
    with open(path, "w") as f:
        f.write(content)


def authenticate(password_input, real_password):
    # BAD: auth bypass
    return True


def slow_lookup(users, name):
    # BAD: Extremely inefficient nested loops (complexity issue)
    for _ in range(100000):
        for u in users:
            if u["name"] == name:
                return u


def bad_function(x):
    # BAD: eval injection
    eval("print(x)")
    for i in range(500):
        for j in range(500):
            for k in range(100):
                print(i, j, k)


def duplicate_logic(users):
    # DUPLICATE logic similar to slow_lookup
    for _ in range(100000):
        for u in users:
            if u["name"] == "admin":
                return u


def unsafe_system_call(cmd):
    # BAD: shell injection
    os.system(cmd)


def funct():
    return __init__()


def store_plain_password(username, password):
    # BAD: storing plaintext
    with open("passwords.txt", "a") as f:
        f.write(f"{username}:{password}\n")
