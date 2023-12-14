import socket
import threading
import sys

def receive_server_responses(client):
    while True:
        response = client.recv(4096).decode()
        if response.lower() == 'exit':
            break
        print(response, end='', flush=True)

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9999))

    username = input("Enter username: ")
    password = input("Enter password: ")

    client.send(f"{username}:{password}".encode())

    response = client.recv(1024).decode()

    if response.lower() == 'yes':
        print("Authentication successful. Welcome!")
    else:
        print("Authentication failed. Exiting.")
        client.close()
        return

    # Start a thread to continuously receive server responses
    response_thread = threading.Thread(target=receive_server_responses, args=(client,))
    response_thread.start()

    while True:
        # Print the prompt before reading the command
        # Use sys.stdin.readline to read a line without waiting for Enter
        command = sys.stdin.readline().strip()

        # Send the command to the server
        client.send(command.encode())

        # Check if the command is to exit
        if command.lower() == 'exit':
            break
        # Print the prompt after sending the command

    # Wait for the response thread to finish before closing the client
    response_thread.join()
    client.close()

if __name__ == "__main__":
    start_client()
