"""
⚠️ Simulated Vulnerable Auth Code
This is for SECURITY TESTING ONLY.
Functions are intentionally weak but safe (no real exploits).
"""

# Fake hardcoded secret (pattern for detection)
SECRET_KEY = "HARDCODED_SECRET_KEY"

# Fake password storage (plaintext, unsafe pattern)
users = {"admin": "password123"}

def register_user(username: str, password: str):
    # ❌ Pretend to store plaintext password
    users[username] = password
    return "User registered (insecure)"

def login_user(username: str, password: str):
    # ❌ Direct comparison (timing attack risk)
    if users.get(username) == password:
        return "Login successful (insecure)"
    return "Login failed"

def generate_token(username: str):
    # ❌ Fake token, no expiry, hardcoded secret
    return f"{username}:{SECRET_KEY}"

def verify_token(token: str):
    # ❌ Just checks if secret is present
    return token.endswith(f":{SECRET_KEY}")
