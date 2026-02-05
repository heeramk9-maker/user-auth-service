"""
⚠️ Simulated Multi-Vulnerability Code
For SECURITY TESTING ONLY — not for production use.
This file intentionally demonstrates insecure patterns:
- SQL injection
- eval misuse
- insecure pickle deserialization
- unsafe socket handling
"""

import sqlite3
import socket
import pickle

# -------------------------------------------------------------------
# DATABASE (bad)
# -------------------------------------------------------------------

def login_user(username: str, password: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # ❌ SQL injection risk: direct string interpolation
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    if result:
        return "Login successful (insecure)"
    return "Login failed"

# -------------------------------------------------------------------
# EVAL (bad)
# -------------------------------------------------------------------

def unsafe_eval(user_input: str):
    # ❌ Arbitrary code execution
    return eval(user_input)

# -------------------------------------------------------------------
# PICKLE (bad)
# -------------------------------------------------------------------

def unsafe_deserialize(data: bytes):
    # ❌ Insecure deserialization
    obj = pickle.loads(data)
    return obj

# -------------------------------------------------------------------
# SOCKET (bad)
# -------------------------------------------------------------------

def start_server():
    # ❌ No TLS, plaintext communication
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8888))  # ❌ Hardcoded port
    s.listen(5)
    print("Insecure server listening...")

    while True:
        conn, addr = s.accept()
        print(f"Connection from {addr}")

        # ❌ No authentication
        data = conn.recv(1024)
        if not data:
            break

        # ❌ Echoes back raw input
        conn.sendall(data)

        # ❌ No error handling
        conn.close()
