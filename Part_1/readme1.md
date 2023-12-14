# Client-Server Application

## Description

This is a simple client-server application that allows users to remotely execute commands on the server and receive responses. The server provides basic file system commands and system information, while the client handles user authentication and command execution.

## Features

- User authentication
- Remote command execution
- File system commands (e.g., ls, mkdir, cd)
- System information retrieval

## Requirements

- Python 3 
- Libraries: `socket`, `threading`, `os`, `psutil`

## Usage

1. **Start the Server:**

    ```bash
    python server.py
    ```

   The server will start listening on port 8080.

2. **Run the Client:**

    ```bash
    python client.py
    ```

   Follow the prompts to enter your username and password. If authentication is successful, you can start entering commands to interact with the server.

   - To exit the client, type `exit`.

## Example Commands

- `ls`: List files in the current directory.
- `mkdir <directory_name>`: Create a new directory.
- `cd <directory_name>`: Change the current directory.
- `echo <message>`: Display a message.
- `<custom_command>`: Execute custom system commands.

## Notes

- The server provides a basic set of commands. Feel free to extend it based on your requirements.
- Ensure that the firewall allows communication on the specified port.


