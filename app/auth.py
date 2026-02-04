"""
⚠️ BAD LOGIN SYSTEM EXAMPLE
- Stores plaintext passwords
- No input validation
- Hardcoded secret key
- Vulnerable to SQL injection
"""

import sqlite3

# -------------------------------------------------------------------
# DATABASE SETUP (bad)
# -------------------------------------------------------------------

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
conn.commit()

# -------------------------------------------------------------------
# USER REGISTRATION (bad)
# -------------------------------------------------------------------

def register_user(username: str, password: str):
    # ❌ Stores plaintext password directly
    cursor.execute(f"INSERT INTO users VALUES ('{username}', '{password}')")
    conn.commit()
    print("User registered!")

# -------------------------------------------------------------------
# USER LOGIN (bad)

        print("Login failed!")
        return False

# -------------------------------------------------------------------
# TOKEN GENERATION (bad)
# -------------------------------------------------------------------

def generate_token(username:
