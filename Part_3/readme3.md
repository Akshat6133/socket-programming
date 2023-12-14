Certainly! Below is the markdown code for the `readme.md` file:

```markdown
# Simple Echo Server-Client Application

## Description

This project comprises a basic echo server-client application. The server listens for incoming connections and echoes back any received data to the connected client. The client connects to the server, sends a message, and receives the echoed response.

## Files

### `server.py`

The server-side script establishes a socket connection and listens for incoming client connections. It echoes back any received data to the client.

### `client.py`

The client-side script connects to the server, sends a user-provided message, and receives the echoed response.

## How to Run

1. **Start the Server:**

   ```bash
   python server.py [port]
   ```

   If a port is not provided, the default port is 8888. The server will listen for incoming connections and echo back received data.

2. **Run the Client:**

   ```bash
   python client.py [host] [port] [message]
   ```

   If host, port, and message are not provided, the default values are localhost, 8888, and a user-input message, respectively. The client connects to the server, sends the message, and prints the echoed response.

## Example Usage

1. **Start the Server:**

   ```bash
   python server.py
   ```

   The server will listen on the default port (8888).

2. **Run the Client:**

   ```bash
   python client.py
   ```

   Follow the prompts to input the message you want to echo. The client will connect to the server, send the message, and display the echoed response.

## Additional Notes

- The default host for the client is localhost, and the default port is 8888.
- The server and client use the `socket` library to establish connections.
- The server echoes back any data received from the client.

