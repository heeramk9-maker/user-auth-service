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

# Load secrets from environment (never hardcode)
API_KEY = os.getenv("API_KEY", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
JWT_SECRET = os.getenv("JWT_SECRET", "")


# ---------------- PASSWORD HASHING ----------------

def hash_password(password: str, salt: Optional[bytes] = None) -> str:
    """
    Secure password hashing using PBKDF2-HMAC-SHA256 + random salt.
    Returns: salt:hash (hex encoded)
    """
    if salt is None:
        salt = secrets.token_bytes(16)

    pwd_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000
    )
    return f"{salt.hex()}:{pwd_hash.hex()}"


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify password against stored salted hash safely.
    """
    try:
        salt_hex, hash_hex = password_hash.split(":")
        salt = bytes.fromhex(salt_hex)

        check_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            100_000
        ).hex()

        # Prevent timing attacks
        return hmac.compare_digest(check_hash, hash_hex)
    except Exception:
        return False


# ---------------- SESSION TOKEN ----------------

def generate_session_token(username: str) -> str:
    """
    Generate cryptographically secure session token.
    """
    random_part = secrets.token_hex(32)
    raw = f"{username}:{random_part}:{time.time()}"
    return hashlib.sha256(raw.encode()).hexdigest()


# ---------------- SAFE AUTH ----------------

def authenticate_user(
    username: str,
    password_input: str,
    user_store: Dict[str, str]
) -> Optional[str]:
    """
    Authenticate user and return session token if valid.
    user_store: {username: password_hash}
    """
    stored_hash = user_store.get(username)
    if not stored_hash:
        return None

    if verify_password(password_input, stored_hash):
        return generate_session_token(username)

    return None


# ---------------- SAFE LOOKUP ----------------

def find_user(users: List[Dict], name: str) -> Optional[Dict]:
    """
    Efficient user lookup (O(n))
    """
    for user in users:
        if user.get("name") == name:
            return user
    return None


# ---------------- SAFE UTILITIES ----------------

def safe_read_file(base_dir: str, filename: str) -> str:
    """
    Prevent path traversal attacks when reading files.
    """
    safe_path = os.path.abspath(os.path.join(base_dir, filename))

    if not safe_path.startswith(os.path.abspath(base_dir)):
        raise PermissionError("Invalid file path")

    with open(safe_path, "r", encoding="utf-8") as f:
        return f.read()


def safe_write_file(base_dir: str, filename: str, content: str) -> None:
    """
    Prevent arbitrary file write.
    """
    safe_path = os.path.abspath(os.path.join(base_dir, filename))

    if not safe_path.startswith(os.path.abspath(base_dir)):
        raise PermissionError("Invalid file path")

    with open(safe_path, "w", encoding="utf-8") as f:
        f.write(content)
