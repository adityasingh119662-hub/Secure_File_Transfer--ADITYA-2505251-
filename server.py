import socket

HOST = '0.0.0.0'
PORT = 5001

server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on port {PORT}...")

conn, addr = server_socket.accept()
print(f"Connection from: {addr}")

with open("received_encrypted_file", "wb") as file:
    while True:
        data = conn.recv(1024)

        if not data:
            break

        file.write(data)

print("Encrypted file received successfully!")

conn.close()
server_socket.close()
