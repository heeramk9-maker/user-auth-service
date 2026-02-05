


import socket

# -------------------------------------------------------------------
# SOCKET + PICKLE (bad)
# -------------------------------------------------------------------

def bad_socket_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 9999))   # ❌ Hardcoded port, binds everywhere
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connection from {addr}")

    data = conn.recv(1024)
    # ❌ Insecure deserialization
    obj = pickle.loads(data)
    print("Received object:", obj)

    conn.sendall(b"Processed insecurely")
    conn.close()

# -------------------------------------------------------------------
# FILE HANDLING (bad)
# -------------------------------------------------------------------

def write_file(content: str):
    # ❌ World-writable file, no validation
    with open(FILE_PATH, "w") as f:
        f.write(content)
    os.chmod(FILE_PATH, 0o777)
    return "File written (insecure)"

# -------------------------------------------------------------------
# EVAL (bad)
# -------------------------------------------------------------------

def unsafe_eval(user_input: str):
    # ❌ Arbitrary code execution
    return eval(user_input)

# -------------------------------------------------------------------
# DATABASE (bad)
# -------------------------------------------------------------------


    if result:
        return "Login successful (insecure)"
    return "Login failed"

