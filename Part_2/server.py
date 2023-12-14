import socket

def load_dns_mapping():
    dns_mapping = {}
    with open("dns_mapping.txt", "r") as file:
        for line in file:
            domain, ip = line.strip().split()
            dns_mapping[domain] = ip
    return dns_mapping

def handle_dns_request(data):
    try:
        transaction_id, domain_name = data.decode().split(',')
        transaction_id = int(transaction_id)

        dns_mapping = load_dns_mapping()
        ip_address = dns_mapping.get(domain_name, "Not Found")

        response = f"{transaction_id},{ip_address}".encode()
        return response
    except Exception as e:
        print(f"Error handling DNS request: {e}")
        return b"Error"

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("localhost", 12345)
    server_socket.bind(server_address)

    print("DNS Server is listening on", server_address)

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print("Received DNS request from", client_address)

        response_data = handle_dns_request(data)
        server_socket.sendto(response_data, client_address)

if __name__ == "__main__":
    main()
