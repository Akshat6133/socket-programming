import socket
import sys

def echo_server(host, port):
    # Create a socket using getaddrinfo
    addrinfo = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
    (family, socktype, proto, _, sockaddr) = addrinfo[0]

    server_socket = socket.socket(family, socktype, proto)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(sockaddr)
    server_socket.listen(1)

    print(f"Echo server is listening on {host}:{port}")

    while True:
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        data = client_socket.recv(1024)
        while data:
            print(f"Received: {data.decode('utf-8')}")
            client_socket.sendall(data)
            data = client_socket.recv(1024)

        print("Connection closed")
        client_socket.close()

if __name__ == "__main__":
    host = "::"
    port = 8888

    if len(sys.argv) == 2:
        port = int(sys.argv[1])

    echo_server(host, port)
