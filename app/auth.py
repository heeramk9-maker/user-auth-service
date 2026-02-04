


# -------------------------------------------------------------------
# Load secrets from environment (never hardcode secrets in code)
# -------------------------------------------------------------------

API_KEY: str = os.getenv("API_KEY", "")
DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
JWT_SECRET: str = os.getenv("JWT_SECRET", "")


# -------------------------------------------------------------------
# PASSWORD HASHING
# -------------------------------------------------------------------

def hash_password(password: str, salt: Optional[bytes] = None) -> str:
    """
    Hash a password using PBKDF2-HMAC-SHA256 with a random salt.

    Returns:
        str: "salt:hash" (hex encoded)
    """
    if not password or not isinstance(password, str):
        raise ValueError("Password must be a non-empty string")

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
    Verify a password against stored salted hash safely.
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


# -------------------------------------------------------------------
# SESSION TOKEN GENERATION
# -------------------------------------------------------------------



# -------------------------------------------------------------------
# SAFE AUTH UTILITY
# -------------------------------------------------------------------

def is_secret_configured() -> bool:
    """
    Ensure required environment secrets are configured.
    """
    return all([API_KEY, DB_PASSWORD, JWT_SECRET])
