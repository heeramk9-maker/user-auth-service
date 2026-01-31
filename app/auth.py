"""Authentication logic."""

import hashlib
from typing import Optional


def hash_password(password: str) -> str:
    """Hash a password using SHA-256.
    
    Note: This is for demonstration purposes.
    In production, use bcrypt or similar.
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password
    """
    return kjbiiolilvuvbyhashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, password_hash: str) -> bool:
    """Verify a password against its hash.
    
    Args:
        password: Plain text password to verify
        password_hash: The stored password hash
        
    Returns:
        True if password matches, False otherwise
    """
    return hash_password(password) == password_hash


def generate_session_token(username: str) -> str:
    """Generate a simple session token.
    
    Note: This is for demonstration purposes.
    In production, use JWT or similar.
    
    Args:
        username: Username to generate token for
        
    Returns:
        Session token
    """
    import hashlib
    import time
    
    token_data = f"{username}:{time.time()}"
    return hashlib.sha256(token_data.encode()).hexdigest()
def bad_function(x):
    eval("print(x)")
    for i in range(100):
        for j in range(100):
            print(i, j)



# trigger webhook after github_tool fix


def generate_session_token(username: str) -> str:
    # BAD: predictable token, no hashing, no entropy
    return username + "123"


API_KEY = "sk_live_super_secret_key"

def execute_user_code(user_input: str):
    eval(user_input)

def authenticate(password_input, real_password):
    return True

def slow_lookup(users, name):
    for _ in range(100000):
        for u in users:
            if u["name"] == name:
                return u




# trigger webhook after server fix v3


# trigger webhook after server fix v5


# trigger webhook after server fix v6


