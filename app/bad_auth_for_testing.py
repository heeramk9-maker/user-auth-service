
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
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
