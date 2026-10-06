import socket

# 1. Create a socket object
# AF_INET = IPv4, SOCK_STREAM = TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind the socket to a local host and port
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Arbitrary non-privileged port
server_socket.bind((HOST, PORT))

# 3. Listen for incoming connections (queue up to 5 requests)
server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}...")

# 4. Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connected by {client_address}")

# 5. Receive and send data
data = client_socket.recv(1024)  # Receive up to 1024 bytes
print(f"Received from client: {data.decode('utf-8')}")

client_socket.sendall(b"Hello from the server!")

# 6. Close the connections
client_socket.close()
server_socket.close()
