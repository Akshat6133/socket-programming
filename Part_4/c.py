import socket

def start_client():
    host = '127.0.0.1'
    port = 12345
    buffer_size = 1024

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))

        filename = input("please type the name of the file you want to share: ")
        client_socket.send(filename.encode('utf-8'))

        with open('received_' + filename, 'wb') as file:
            data = client_socket.recv(buffer_size)
            while data:
                file.write(data)
                data = client_socket.recv(buffer_size)

        print(f"File received successfully from {host}:{port}")

    except Exception as e:
        print(f"Error receiving file: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
