"""
⚠️ Simulated Multi-Vulnerability Code
For SECURITY TESTING ONLY — not for production use.
This file intentionally demonstrates insecure patterns:
- Socket misuse
- Insecure pickle deserialization
- Arbitrary eval
- Unsafe file handling
- SQL injection
"""

import socket
import pickle
import os
import sqlite3

# ❌ Hardcoded file path and DB file
FILE_PATH = "/tmp/important.txt"
DB_FILE = "users.db"

# -------------------------------------------------------------------
# SOCKET + PICKLE (bad)
# -------------------------------------------------------------------

def bad_socket_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 9999))   # ❌ Hardcoded port, binds everywhere
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connection from {addr}")

    data = conn.recv(1024)
    # ❌ Insecure deserialization
    obj = pickle.loads(data)
    print("Received object:", obj)

    conn.sendall(b"Processed insecurely")
    conn.close()

# -------------------------------------------------------------------
# FILE HANDLING (bad)
# -------------------------------------------------------------------

def write_file(content: str):
    # ❌ World-writable file, no validation
    with open(FILE_PATH, "w") as f:
        f.write(content)
    os.chmod(FILE_PATH, 0o777)
    return "File written (insecure)"

# -------------------------------------------------------------------
# EVAL (bad)
# -------------------------------------------------------------------

def unsafe_eval(user_input: str):
    # ❌ Arbitrary code execution
    return eval(user_input)

# -------------------------------------------------------------------
# DATABASE (bad)
# -------------------------------------------------------------------


    if result:
        return "Login successful (insecure)"
    return "Login failed"

# ❌ Dangerous execution at import time
print("Starting vulnerable service...")
os.system("echo Service running with secrets")
