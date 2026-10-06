import socket

# 1. Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to the server
HOST = '127.0.0.1'
PORT = 65432
client_socket.connect((HOST, PORT))

# 3. Send data
client_socket.sendall(b"Hello from the client!")

# 4. Receive a response
data = client_socket.recv(1024)
print(f"Received from server: {data.decode('utf-8')}")

# 5. Close the socket
client_socket.close()
