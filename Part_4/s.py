import socket
import os

def start_server():
    host = '127.0.0.1'
    port = 12345
    buffer_size = 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        try:
            # Receive the filename
            filename = client_socket.recv(buffer_size).decode('utf-8')

            # Open the file and send its content in chunks
            with open(filename, 'rb') as file:
                data = file.read(buffer_size)
                while data:
                    client_socket.send(data)
                    data = file.read(buffer_size)

            print(f"File sent successfully to {addr}")

        except Exception as e:
            print(f"Error sending file to {addr}: {e}")

        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()



