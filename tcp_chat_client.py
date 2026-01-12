# tcp_chat_client.py
import socket
import threading

server_host = "127.0.0.1"
server_port = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))
print("Connected to server")


def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"\nServer: {data}")
        except:
            break


# Thread to receive messages
threading.Thread(target=receive_messages, daemon=True).start()

# Main thread handles sending
try:
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        client_socket.send(msg.encode())
except KeyboardInterrupt:
    print("\nClient closed")
finally:
    client_socket.close()
