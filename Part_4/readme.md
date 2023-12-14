# File Transfer System

This simple file transfer system consists of a server (`server.py` or `s.py`) and a client (`client.py` or `c.py`). Follow the instructions below to run the system:

## How to Run

1. **Server Setup:**
   - Open a terminal and navigate to the project directory.
   - Run the server script:

     ```bash
     python server.py
     ```

2. **Client Setup:**
   - Open another terminal window.
   - Run the client script:

     ```bash
     python client.py
     ```

   - You will be prompted to enter the name of the file you want to share.

3. **File Transfer:**
   - After running the client script, type the name of the file you want to share (e.g., `<file>`).
   - The server will receive the request and fetch the specified file.
   - The client will save the received file with the filename as "received_<file>".

4. **Verification:**
   - Run the following command in the terminal to confirm whether the received file is empty or not:

     ```bash
     cat received_<file>
     ```

**Note:** Ensure that both the server and client scripts are running on the same machine.

## File Structure

- `server.py` (or `s.py`): The server script that listens for client connections, receives file requests, and sends the requested file back to the client.

- `client.py` (or `c.py`): The client script that connects to the server, sends a file request, and receives the requested file from the server.

## Dependencies

- Python 3.x

## Contributors

- Your Name
- Your Email

