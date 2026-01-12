# tcp_file_client.py 
import socket
import os

server_host = "127.0.0.1"
server_port = 65433

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))
print("Connected to server. Type 'exit' to quit.")

try:
    while True:
        filepath = input("Enter full path of file to send: ")
        if filepath.lower() == "exit":
            client_socket.send("exit".encode())
            break
        if not os.path.exists(filepath):
            print("File not found! Try again.")
            continue

        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)

        # send file path and size
        client_socket.send(filepath.encode())
        client_socket.send(str(filesize).encode())

        # send file in chunks
        sent = 0
        with open(filepath, "rb") as f:
            data = f.read(1024)
            while data:
                client_socket.send(data)
                sent += len(data)
                data = f.read(1024)
                print(f"\rSent {sent}/{filesize} bytes", end="")
        print(f"\nFile {filename} sent successfully!\n")
finally:
    client_socket.close()
