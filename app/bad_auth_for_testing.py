"""
⚠️ Simulated Vulnerable Networking Code
For SECURITY TESTING ONLY — not for production use.
This file intentionally demonstrates insecure socket handling.
"""

import socket

# ❌ Hardcoded host and port
HOST = "0.0.0.0"   # binds to all interfaces
PORT = 12345       # fixed port, no config

def start_server():
    # ❌ No TLS, plaintext communication
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Insecure server listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        print(f"Connection from {addr}")

        # ❌ No authentication, accepts any client
        data = conn.recv(1024)
        if not data:
            break

        # ❌ Echoes back raw input (potential injection risk)
        conn.sendall(data)

        # ❌ No logging, no error handling
        conn.close()

def insecure_client(message: str):
    # ❌ Connects without validation
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(message.encode())
    response = s.recv(1024)
    s.close()
    return response.decode()
