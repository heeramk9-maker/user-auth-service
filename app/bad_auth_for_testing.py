"""
⚠️ Simulated Vulnerable Database Code
For SECURITY TESTING ONLY — not for production use.
This file intentionally demonstrates insecure SQL handling.
"""


# ❌ Hardcoded database file
DB_FILE = "users.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # ❌ No constraints, stores plaintext passwords
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()

def register_user(username: str, password: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # ❌ Direct string interpolation → SQL injection risk
    cursor.execute(f"INSERT INTO users VALUES ('{username}', '{password}')")
    conn.commit()
    conn.close()
    return "User registered (insecure)"

def login_user(username: str, password: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # ❌ Vulnerable query, attacker can bypass with crafted input
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    result = cursor.fetchone()
    conn.close()
    if result:
        return "Login successful (insecure)"
    return "Login failed"

def delete_user(username: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # ❌ Deletes without confirmation, no audit trail
    cursor.execute(f"DELETE FROM users WHERE username='{username}'")
    conn.commit()
    conn.close()
    return "User deleted (insecure)"
