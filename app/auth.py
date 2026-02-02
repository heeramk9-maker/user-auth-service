"""
Authentication logic — FIXED VERSION
Secure implementation for password handling, tokens, and file access.
"""

import hashlib
import os
import secrets
import time
from typing import Optional, List, Dict

# Load secrets from environment (never hardcode)
API_KEY = os.getenv("API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")
JWT_SECRET = os.getenv("JWT_SECRET")


# ---------------- PASSWORD HASHING ----------------

def hash_password(password: str, salt: Optional[bytes] = None) -> str:
    """
    Secure password hashing using SHA-256 + salt.
    """
    if not salt:
        salt = secrets.token_bytes(16)

    pwd_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )
    return salt.hex() + ":" + pwd_hash.hex()


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify password against stored salted hash.
    """
    salt_hex, hash_hex = password_hash.split(":")
    salt = bytes.fromhex(salt_hex)

    check_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    ).hex()

    return check_hash == hash_hex


# ---------------- SESSION TOKEN ----------------

def generate_session_token(username: str) -> str:
    """
    Generate cryptographically secure session token.
    """
    random_part = secrets.token_hex(32)
    return hashlib.sha256(f"{username}:{random_part}:{time.time()}".encode()).hexdigest()


# ---------------- SAFE AUTH ----------------

def authenticate(password_input: str, real_password_hash: str) -> bool:
    """
    Proper authentication check.
    """
    return verify_password(password_input, real_password_hash)


# ---------------- SAFE LOOKUP ----------------

def fast_lookup(users: List[Dict], name: str) -> Optional[Dict]:
    """
    Efficient lookup using dictionary indexing.
    """
    user_map = {u["name"]: u for u in users}
    return user_map.get(name)


# ---------------- SAFE UTILITIES ----------------

def read_safe_file(path: str, base_dir: str = "./data") -> str:
    """
    Restrict file reading to a safe directory.
    """
    full_path = os.path.abspath(os.path.join(base_dir, path))
    if not full_path.startswith(os.path.abspath(base_dir)):
        raise PermissionError("Unauthorized file access")

    with open(full_path, "r") as f:
        return f.read()



