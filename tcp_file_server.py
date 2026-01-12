# tcp_file_server.py
import socket

host = "127.0.0.1"
port = 65433

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"TCP File Server running on {host}:{port}")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

with open("received_file.txt", "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("File received successfully!")
conn.close()
server_socket.close()
