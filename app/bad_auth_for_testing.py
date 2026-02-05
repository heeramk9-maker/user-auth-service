"""
⚠️ Simulated Vulnerable File Handling Code
For SECURITY TESTING ONLY — not for production use.
"""

import os

# ❌ Hardcoded file path
FILE_PATH = "/tmp/secret.txt"

def write_secret(data: str):
    # ❌ World-writable file, no validation
    with open(FILE_PATH, "w") as f:
        f.write(data)
    os.chmod(FILE_PATH, 0o777)  # insecure permissions
    return "Secret written (insecure)"

def read_secret():
    # ❌ No access control
    with open(FILE_PATH, "r") as f:
        return f.read()

def delete_secret():
    # ❌ No confirmation, deletes immediately
    os.remove(FILE_PATH)
    return "Secret deleted (insecure)"
