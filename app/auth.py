"""
Authentication logic — SECURE FINAL VERSION
"""

import os
import hashlib
import hmac
import secrets
import time


# ---------------- ENV VALIDATION ----------------

def _get_env_or_fail(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


API_KEY = _get_env_or_fail("API_KEY")
DB_PASSWORD = _get_env_or_fail("DB_PASSWORD")
JWT_SECRET = _get_env_or_fail("JWT_SECRET")


# ---------------- PASSWORD HASHING ----------------

def hash_password(password: str, salt: bytes | None = None) -> str:
    """
    PBKDF2-HMAC-SHA256 with salt.
    Returns 'salt:hash'
    """
    if not password or len(password) < 8:
        raise ValueError("Password too short")

    if salt is None:
        salt = secrets.token_bytes(16)

    pwd_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000,
    )

    return f"{salt.hex()}:{pwd_hash.hex()}"


def verify_password(password: str, stored: str) -> bool:
    """
    Safe constant-time password verification
    """
    try:
        salt_hex, hash_hex = stored.split(":")
        salt = bytes.fromhex(salt_hex)

        new_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt,
            100_000,
        ).hex()

        return hmac.compare_digest(new_hash, hash_hex)

    except Exception:
        return False


# ---------------- SESSION TOKEN ----------------

def generate_session_token(username: str) -> str:
    """
    Secure session token (hex string)
    """
    raw = f"{username}:{secrets.token_hex(32)}:{time.time()}"
    return hashlib.sha256(raw.encode()).hexdigest()
