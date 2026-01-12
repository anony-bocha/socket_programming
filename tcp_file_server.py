# tcp_file_server.py (modern version)
import socket
import os

host = "127.0.0.1"
port = 65433

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"TCP File Server running on {host}:{port}")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

try:
    while True:
        filepath = conn.recv(1024).decode()
        if not filepath or filepath.lower() == "exit":
            break
        filename = os.path.basename(filepath)  # keep original file name

        filesize = int(conn.recv(1024).decode())
        print(f"Receiving {filename} ({filesize} bytes)...")

        with open(filename, "wb") as f:
            received = 0
            while received < filesize:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
                received += len(data)
                print(f"\rProgress: {received}/{filesize} bytes", end="")
        print(f"\nFile {filename} received successfully!\n")
finally:
    conn.close()
    server_socket.close()
