# tcp_chat_client.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = "127.0.0.1"
server_port = 65432

client_socket.connect((server_host, server_port))
print("Connected to server")

try:
    while True:
        msg = input("You: ")
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Server: {data}")
except KeyboardInterrupt:
    print("\nClient closed by user")
finally:
    client_socket.close()
