"""
⚠️ BAD AUTHENTICATION EXAMPLE
- Plaintext password storage
- Weak hashing (SHA1 without salt)
- Hardcoded secret key
- No token expiry or validation
"""

import hashlib

# -------------------------------------------------------------------
# USER DATABASE (bad)
# -------------------------------------------------------------------

users = {}  # ❌ In-memory dict, stores plaintext passwords

def register_user(username: str, password: str):
    # ❌ Hashing with SHA1, no salt
    hashed = hashlib.sha1(password.encode()).hexdigest()
    users[username] = hashed
    print("User registered!")

def login_user(username: str, password: str) -> bool:
    # ❌ Direct comparison, no timing attack protection
    hashed = hashlib.sha1(password.encode()).hexdigest()
    if users.get(username) == hashed:
        print("Login successful!")
        return True
    else:
        print("Login failed!")
        return False

# -------------------------------------------------------------------
# TOKEN GENERATION (bad)
# -------------------------------------------------------------------

def generate_token(username: str) -> str:
    # ❌ Hardcoded secret, no expiry
    secret = "mysecret"
    return f"{username}:{secret}"

def verify_token(token: str) -> bool:
    # ❌ Just checks if secret is present, no signature validation
    return token.endswith(":mysecret")

