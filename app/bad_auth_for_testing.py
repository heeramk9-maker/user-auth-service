
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
        data = conn.recv(4096)  # large buffer, no limits
        if not
        # ❌ Echoes back raw input (potential injection risk)
        conn.sendall(data)

        # ❌ No logging, no error handling
        conn.close()
    # ❌ Connects without validation

    # ❌ Sends credentials in plaintext
    s.sendall(f"{USERNAME}:{PASSWORD}\n".encode())

    # ❌ Sends arbitrary message
    s.sendall(message.encode())

    response = s.recv(4096)
    s.close()
    return response.decode()
