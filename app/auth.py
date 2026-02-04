 """
Authentication logic — FIXED VERSION
Secure
    if salt is None:
        salt = secrets.token_bytes(16)

    pwd_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000,
    )

  


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify password against stored salted hash safely.
    """
    try:
        salt_hex, stored_hash_hex = password_hash.split(":")
        salt = bytes.fromhex(salt_hex)

   

        

    except Exception:
        return False


# ---------------- SESSION TOKEN ----------------




# ---------------- SAFE AUTH ----------------




