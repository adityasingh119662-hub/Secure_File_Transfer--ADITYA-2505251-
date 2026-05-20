import socket

SERVER_IP = '10.137.12.176'
PORT = 5001

client_socket = socket.socket()
client_socket.connect((SERVER_IP, PORT))

with open("encrypted_sample.txt", "rb") as file:
    while True:
        data = file.read(1024)

        if not data:
            break

        client_socket.send(data)

print("Encrypted file sent successfully!")

client_socket.close()