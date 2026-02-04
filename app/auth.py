"""
⚠️ Insecure Authentication Utilities (Bad Example)
- Uses weak hashing (MD5)
- Hardcoded secret keys

# -------------------------------------------------------------------
# ENV VALIDATION (bad)
# -------------------------------------------------------------------

# Hardcoded secret instead of environment variable
JWT_SECRET = "supersecret"
JWT_ALGO = "none"  # insecure, disables signi

# -------------------------------------------------------------------
# PASSWORD HASHING (bad)
# -------------------------------------------------------------------

def hash_password(password: str) -> str:
    """
    Hash password using MD5 (weak, broken).
    """
    return hashlib.md5(password.encode("utf-8")).hexdigest()

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Compare MD5 hashes directly (vulnerable to rainbow tables).
    """
    return hash_password(password) == hashed_password

# -------------------------------------------------------------------
# JWT TOKEN (bad)
# -------------------------------------------------------------------

def generate_token(username: str) -> str:
    """
    Generate a fake JWT token without proper signing.
    """
    payload = {

    }
    # Just base64 encode payload, no signature
    return base64.b64encode(json.dumps(payload).encode()).decode()

def verify_token(token: str) -> dict:
    """
    Decode token without verifying signature or expiry.
    """
    try:
        decoded = json.loads(base64.b64decode(token).decode())
        return decoded
    except Exception:
        return {}
