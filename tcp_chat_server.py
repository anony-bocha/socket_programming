# tcp_chat_server.py
import socket
import threading

host = "127.0.0.1"
port = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"TCP Chat Server running on {host}:{port}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")


def receive_messages():
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"\nClient: {data}")
        except:
            break


# Start thread to receive messages
threading.Thread(target=receive_messages, daemon=True).start()

# Main thread handles sending
try:
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        conn.send(msg.encode())
except KeyboardInterrupt:
    print("\nServer closed")
finally:
    conn.close()
    server_socket.close()
