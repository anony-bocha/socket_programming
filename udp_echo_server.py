# udp_echo_server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("127.0.0.1", 12345))

print("UDP Echo Server is running...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received from {client_address}: {data.decode()}")

    server_socket.sendto(data, client_address)
