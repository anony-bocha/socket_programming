# udp_echo_client.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter message: ")

client_socket.sendto(message.encode(), ("127.0.0.1", 12345))

data, server_address = client_socket.recvfrom(1024)
print("Echo from server:", data.decode())

client_socket.close()
