# tcp_file_client.py
import socket

server_host = "127.0.0.1"
server_port = 65433

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))
print("Connected to server")

filename = input("Enter file name to send: ")

try:
    with open(filename, "rb") as f:
        data = f.read(1024)
        while data:
            client_socket.send(data)
            data = f.read(1024)
    print("File sent successfully!")
except FileNotFoundError:
    print("File not found!")

client_socket.close()
