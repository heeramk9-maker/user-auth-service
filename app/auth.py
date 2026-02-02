  """
Authentication logic — FIXED VERSION
Secure implementation for password handling, tokens, and safe utilities.
"""
import hashlib
import hmac
import os 
import secrets
import time
from typing import Optional, Dict, List   

# Load secrets from environment (never hardcode
API_KEY = os.getenv("API_KEY", "") 
DB_PASSWORD = os.getenv("DB_PASSWORD", "")  
JWT_SECRET = os.getenv("JWT_SECRET", "")

# ---------------- PASSWORD HASHING ---------------

def hash_password(password: str, salt: Optional[bytes] = None) 
    """
    Secure password hashing using PBKDF2-HMAC-SHA256 + random salt.
    Returns: salt:hash
    """
    if salt is None:
        salt = secrets.token_bytes(16)

    pwd_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000,
    )

    return f"{salt.hex()}:{pwd_hash.hex()}"


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify password against stored salted hash safely.
    """
    try:
        salt_hex, stored_hash_hex = password_hash.split(":")
        salt = bytes.fromhex(salt_hex)

        new_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            100_000,
        ).hex()

        return hmac.compare_digest(new_hash, stored_hash_hex)

    except Exception:
        return False


# ---------------- SESSION TOKEN ----------------

def generate_session_token(username: str) -> str:
    """
    Generate secure session token.
    """
    raw = f"{username}:{secrets.token_hex(32)}:{time.time()}"
    return hashlib.sha256(raw.encode())


# ---------------- SAFE AUTH ----------------




