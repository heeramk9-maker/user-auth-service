"""
⚠️ Simulated Very Vulnerable Networking Code
For SECURITY TESTING ONLY — not for production use.


    # ❌ No TLS, plaintext communicatio
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)  # arbitrary backlog
    print(f"Insecure server listening on {HOST}:{PORT}")

    while True
        conn, addr = s.accept()
        print(f"Connection from {addr}")

        # ❌ No authentication, accepts any client
        data = conn.recv(4096)  # large buffer, no limits
        if not data:
            break

        # ❌ Executes received data unsafely (simulated)
        try:
            # Insecure pattern: pretending to run commands
            os.system(data.decode())  # unsafe execution
        except Exception:
            pass

        # ❌ Echoes back raw input (potential injection risk)
        conn.sendall(data)

        # ❌ No logging, no error handling
        conn.close()

def insecure_client(message: str):
    # ❌ Connects without validation
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # ❌ Sends credentials in plaintext
    s.sendall(f"{USERNAME}:{PASSWORD}\n".encode())

    # ❌ Sends arbitrary message
    s.sendall(message.encode())

    response = s.recv(4096)
    s.close()
    return response.decode()
