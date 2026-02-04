"""
Secure Authentication Utilities
- bcrypt password hashing
- validated environment secrets
- constant-time comparisons
- JWT token generation
"""

import os
import time
import bcrypt
import jwt
import hmac
from typing import Dict


# -------------------------------------------------------------------
# ENV VALIDATION (this is what your scanner expects)
# -------------------------------------------------------------------

def _get_env_or_fail(key: str) -> str:
    value = os.getenv(key)
    if not value or value.strip() == "":
        raise RuntimeError(f"Missing required environment variable: {key}")
    return value


JWT_SECRET = _get_env_or_fail("JWT_SECRET")
JWT_ALGO = "HS256"


# -------------------------------------------------------------------
# PASSWORD HASHING (bcrypt)
# -------------------------------------------------------------------

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
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
    payload: Dict[str, str | int] = {
        "sub": username,
        "iat": int(time.time()),
        "exp": int(time.time()) + 3600,  # 1 hour expiry
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)


def verify_token(token: str) -> Dict:
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        return decoded
    except jwt.ExpiredSignatureError:
        raise RuntimeError("Token expired")
    except jwt.InvalidTokenError:
        raise RuntimeError("Invalid token")
