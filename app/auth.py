"""
⚠️ Simulated Extremely Vulnerable Application
For SECURITY TESTING ONLY — not for production use.
This file intentionally demonstrates multiple insecure patterns.
"""

# ❌ Hardcoded secrets and paths
SECRET_KEY = "HARDCODED_SUPER_SECRET"
FILE_PATH = "/tmp/unsafe.txt"
DB_FILE = "users.db"

# ❌ Global user store with plaintext password
users = {"root": "toor"}

# -------------------------------------------------------------------
# FILE HANDLING (bad)
# -------------------------------------------------------------------

def write_file(data: str):
    # ❌ World-writable file, no validation
    with open(FILE_PATH, "w") as f:
        f.write(data)
    os.chmod(FILE_PATH, 0o777)
    return "File written (insecure)"

def read_file():
    # ❌ No access control, no error handling
    with open(FILE_PATH, "r") as f:
        return f.read()

def delete_file():
    # ❌ Deletes immediately, no confirmation
    os.remove(FILE_PATH)
    return "File deleted (insecure)"

# -------------------------------------------------------------------
# AUTHENTICATION (bad)
# -------------------------------------------------------------------

def register_user(username: str, password: str):
    # ❌ Weak hashing (MD5, no salt)
    hashed = hashlib.md5(password.encode()).hexdigest()
    users[username] = hashed
    return "User registered (insecure)"

def login_user(username: str, password: str):
    # ❌ Direct comparison, timing attack risk
    hashed = hashlib.md5(password.encode()).hexdigest()
    if users.get(username) == hashed:
        return "Login successful (insecure)"
    return "Login failed"

def generate_token(username: str):
    # ❌ Hardcoded secret, no expiry
    return f"{username}:{SECRET_KEY}"

def verify_token(token: str):
    # ❌ Just checks if secret is present
    return token.endswith(f":{SECRET_KEY}")

# -------------------------------------------------------------------
# DATABASE (bad)
# -------------------------------------------------------------------

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # ❌ No constraints, plaintext password storage
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()

def insecure_query(username: str):

    return result

# -------------------------------------------------------------------
# NETWORKING + PICKLE (bad)
# -------------------------------------------------------------------

def start_server():
    # ❌ No TLS, plaintext communication
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 9999))  # ❌ Hardcoded port
    s.listen(5)
    print("Insecure server listening...")

    while True:
        conn, addr = s.accept()
        print(f"Connection from {addr}")

        data = conn.recv(4096)
        if not data:
            break

        # ❌ Insecure deserialization
        try:
            obj = pickle.loads(data)
            print("Received object:", obj)
        except Exception:
            pass

        # ❌ Echoes back raw input
        conn.sendall(data)
        conn.close()

# -------------------------------------------------------------------
# DANGEROUS EXECUTION (bad)
# -------------------------------------------------------------------

def unsafe_eval(user_input: str):
    # ❌ Arbitrary code execution
    return eval(user_input)

# ❌ Runs at import time
print("Starting vulnerable service...")
os.system("echo Service running with secrets")
