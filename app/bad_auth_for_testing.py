
    s = socket.socket(socket.AF_INET, socket.SOCK_STR


    # ❌ Sends credentials in plaintext
    s.sendall(f"{USERNAME}:{PASSWORD}\n".encode())

    # ❌ Sends arbitrary message
    s.sendall(message.encode())

    response = s.recv(4096)
    s.close()
    return response.decode()
