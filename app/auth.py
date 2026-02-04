"""
Secure Authentication Utilities

Provides:
- bcrypt-based password hashing
- validated environment secret loading
- JWT token generation and verification
"""

import os
import time
import bcrypt
import jwt


# -------------------------------------------------------------------
# ENV VALIDATION
# -------------------------------------------------------------------

def _get_env_or_fail(key: str) -> str:
    """Fetch required environment variable or raise error."""
    value = os.getenv(key)
    if not value or value.strip() == "":
        raise RuntimeError(f"Missing required environment variable: {key}")
    return value


JWT_SECRET = _get_env_or_fail("JWT_SECRET")
JWT_ALGO = "HS256"


# -------------------------------------------------------------------
# PASSWORD HASHING
# -------------------------------------------------------------------

def hash_password(password: str) -> str:
    """
    Hash a plain-text password using bcrypt with automatic salt.
    Returns the hashed password as a string.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify a plain-text password against a bcrypt hash.
    Returns True if match, otherwise False.
    """
    try:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )
    except Exception:
        return False


# -------------------------------------------------------------------
# JWT TOKEN
# -------------------------------------------------------------------

def generate_token(username: str) -> str:
    """
    Generate a JWT token for a given username with 1-hour expiry.
    """
    payload = {
        "sub": username,
        "iat": int(time.time()),
        "exp": int(time.time()) + 3600,
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)


def verify_token(token: str) -> dict:
    """
    Decode and validate a JWT token.
    Returns the decoded payload if valid.
    Raises RuntimeError if invalid or expired.
    """
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
    except jwt.ExpiredSignatureError:
        raise RuntimeError("Token expired")
    except jwt.InvalidTokenError:
        raise RuntimeError("Invalid token")
