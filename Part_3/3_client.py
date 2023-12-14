import socket
import sys

def echo_client(host, port, message):
    # Create a socket using getaddrinfo
    addrinfo = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
    (family, socktype, proto, _, sockaddr) = addrinfo[0]

    client_socket = socket.socket(family, socktype, proto)
    client_socket.connect(sockaddr)

    print(f"Connected to {host}:{port}")

    client_socket.sendall(message.encode('utf-8'))

    data = client_socket.recv(1024)
    print(f"Received: {data.decode('utf-8')}")

    client_socket.close()

if __name__ == "__main__":
    host = "localhost"
    port = 8888
    message = input("please type the message you want to echo: ")
    

    if len(sys.argv) > 1:
        host = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    if len(sys.argv) > 3:
        message = sys.argv[3]

    echo_client(host, port, message)
