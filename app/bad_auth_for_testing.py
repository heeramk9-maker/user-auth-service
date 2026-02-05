"""
Secure Authentication Module
Designed with separation of concerns and secure practices.
"""

import os  
import sqlite3
import bcrypt
import jwt
from datetime import datetime, timedelta
from typing import Optional

# -------------------------------------------------------------------
# Configuration (comes from environment, not hardcoded)
# -------------------------------------------------------------------

DB_FILE = "users.db"
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")  # for local testing only


# -------------------------------------------------------------------
# Database Helpers (no raw SQL building)
# -------------------------------------------------------------------

def _get_conn():
    return sqlite3.connect(DB_FILE)


def init_db():
    with _get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password_hash TEXT NOT NULL
            )
        """)


# -------------------------------------------------------------------
# Password Hashing (bcrypt)
# -------------------------------------------------------------------

def _hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()


def _verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


# -------------------------------------------------------------------
# Token Handling (JWT)
# -------------------------------------------------------------------

def _generate_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# -------------------------------------------------------------------
# Public API (what rest of app uses)
# -------------------------------------------------------------------

def register_user(username: str, password: str) -> str:
    password_hash = _hash_password(password)

    try:
        with _get_conn() as conn:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash),
            )
        return "User registered successfully"
    except sqlite3.IntegrityError:
        return "User already exists"


def login_user(username: str, password: str) -> Optional[str]:
    with _get_conn() as conn:
        cur = conn.execute(
            "SELECT password_hash FROM users WHERE username = ?",
            (username,),
        )
        row = cur.fetchone()

    if not row:
        return None

    stored_hash = row[0]

    if not _verify_password(password, stored_hash):
        return None

    return _generate_token(username)
