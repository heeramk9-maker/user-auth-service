


import socket

# -------------------------------------------------------------------
# SOCKET + PICKLE (bad)
# -------------------------------------------------------------------
password='1234567890'
def bad_socket_server():loads(data)
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

