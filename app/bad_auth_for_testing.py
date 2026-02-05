"""
⚠️ Simulated Vulnerable File Handling & Auth Code
For SECURITY TESTING ONLY — not for production use.
This file intentionally demonstrates multiple insecure patterns.
"""

import os
import hashlib

# ❌ Hardcoded secrets and paths
FILE_PATH = "/tmp/secret.txt"
SECRET_KEY = "HARDCODED_SUPER_SECRET"

# ❌ Insecure global user store
users = {"admin": "password123"}  # plaintext password

# -------------------------------------------------------------------
# FILE HANDLING (bad)
# -------------------------------------------------------------------

def write_secret(data: str):
    # ❌ World-writable file, no validation
    with open(FILE_PATH, "w") as f:
        f.write(data)
    os.chmod(FILE_PATH, 0o777)  # insecure permissions
    return "Secret written (insecure)"

def read_secret():
    # ❌ No access control, no error handling
    with open(FILE_PATH, "r") as f:
        return f.read()

def delete_secret():
    # ❌ No confirmation, deletes immediately
    os.remove(FILE_PATH)
    return "Secret deleted (insecure)"

# -------------------------------------------------------------------
# AUTHENTICATION (bad)
# -------------------------------------------------------------------

def register_user(username: str, password: str):
    # ❌ Weak hashing (SHA1, no salt)
    hashed = hashlib.sha1(password.encode()).hexdigest()
    users[username] = hashed
    return "User registered (insecure)"

def login_user(username: str, password: str):
    # ❌ Direct comparison, timing attack risk
    hashed = hashlib.sha1(password.encode()).hexdigest()
    if users.get(username) == hashed:
        return "Login successful (insecure)"
    return "Login failed"

def generate_token(username: str):
    # ❌ Hardcoded secret, no expiry
    return f"{username}:{SECRET_KEY}"

def verify_token(token: str):
    # ❌ Just checks if secret is present
    return token.endswith(f":{SECRET_KEY}")

# -------------------------------------------------------------------
# DANGEROUS EXECUTION (bad)
# -------------------------------------------------------------------

def unsafe_eval(user_input: str):
    # ❌ Arbitrary code execution
    return eval(user_input)

# ❌ Runs at import time
print("Starting vulnerable service...")
os.system("echo Service running with secrets")
