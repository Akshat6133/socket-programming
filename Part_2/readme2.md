# DNS Server and Client

This project consists of a simple DNS server and client implementation. The DNS server resolves domain names to IP addresses using a predefined mapping, and the client sends DNS requests to the server to obtain IP addresses for specified domain names.

## Files

- `server.py`: Contains the DNS server implementation.
- `client.py`: Contains the DNS client implementation.
- `dns_mapping.txt`: File containing the mapping of domain names to IP addresses.

## How to Use

### DNS Server

1. **Run the DNS Server:**

    ```bash
    python server.py
    ```

   The server will start listening on `localhost:12345`.

2. **Edit `dns_mapping.txt`:**

   Add domain names and their corresponding IP addresses to the `dns_mapping.txt` file, each entry on a new line, separated by a space.

### DNS Client

1. **Run the DNS Client:**

    ```bash
    python client.py
    ```

2. **Enter Domain Name:**

   Input the domain name for which you want to obtain the IP address when prompted.

3. **View Results:**

   The client will display the transaction ID, domain name, and the received IP address from the server.

## Example

Assuming `dns_mapping.txt` contains:


