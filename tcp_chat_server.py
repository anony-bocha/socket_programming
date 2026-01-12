# tcp_chat_server.py
import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 65432

server_socket.bind((host, port))
server_socket.listen(1)  # listen for 1 client

print(f"TCP Chat Server running on {host}:{port}")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

try:
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")
        msg = input("You: ")
        conn.send(msg.encode())
except KeyboardInterrupt:
    print("\nServer closed by user")
finally:
    conn.close()
    server_socket.close()
