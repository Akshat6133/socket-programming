import socket
import threading
import os
import psutil
from datetime import datetime

user_credentials = {'user': 'password'}
last_login_info = {'user': datetime.now().strftime('%a %m-%d-%y')}
machine_name = socket.gethostname()


def get_system_information():
    memory_usage = psutil.virtual_memory().percent
    processes_count = len(psutil.pids())
    ipv4_address = socket.gethostbyname(socket.gethostname())
    return f"Memory usage: {memory_usage}%\nProcesses: {processes_count}\nIPv4 address: {ipv4_address}"

def handle_client(client_socket, username):
    welcome_message = f"Welcome to devicename\n\nSystem information:\n{get_system_information()}\nLast login: {last_login_info[username]}\n"
    welcome_message += f"{username}@{machine_name}$ "
    client_socket.send(welcome_message.encode())

    while True:
        command = client_socket.recv(1024).decode()

        if command.lower() == 'exit':
            break

        if command.startswith("ls"):
            try:
                items = os.listdir()
                output = "\n".join(items)
            except FileNotFoundError:
                output = "Directory not found."
            except Exception as e:
                output = f"Error: {str(e)}"
        elif command.startswith("mkdir"):
            dir_name = command.split(" ")[1]
            os.mkdir(dir_name)
            output = f"Directory '{dir_name}' created."
        elif command.startswith("echo"):
            output = " ".join(command.split(" ")[1:])
        elif command.startswith("cd"):
            dir_name = command.split(" ")[1]
            try:
                os.chdir(dir_name)
                output = f"Changed directory to '{dir_name}'."
            except FileNotFoundError:
                output = f"Directory not found: {dir_name}"
            except Exception as e:
                output = f"Error: {str(e)}"
        else:
            try:
                output = os.popen(command).read()
            except FileNotFoundError:
                output = f"/bin/sh: {command.split()[0]}: command not found"
            except Exception as e:
                output = f"Error: {str(e)}"
        output += '\n'
        output += f"{username}@{machine_name}$ "
        client_socket.send(output.encode())

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)

    print("Server listening on port 9999...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")

        authentication_data = client_socket.recv(1024).decode().split(':')
        username, password = authentication_data[0], authentication_data[1]

        if user_credentials.get(username) == password:
            client_socket.send("yes".encode())
            print(f"Authenticated user: {username}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
            client_handler.start()
        else:
            client_socket.send("no".encode())
            print(f"Authentication failed for user: {username}")
            client_socket.close()

if __name__ == "__main__":
    start_server()
