import socket

def get_dns_request(transaction_id, domain_name):
    return f"{transaction_id},{domain_name}".encode()

def parse_dns_response(response_data):
    transaction_id, ip_address = response_data.decode().split(',')
    return int(transaction_id), ip_address

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("localhost", 12345)

    domain_name = input("Enter the domain name: ")
    transaction_id = hash(domain_name) % 65535

    dns_request = get_dns_request(transaction_id, domain_name)
    client_socket.sendto(dns_request, server_address)
    print(f"Sent DNS request (Transaction ID: {transaction_id}) for {domain_name} to the server")

    response_data, _ = client_socket.recvfrom(1024)

    transaction_id, ip_address = parse_dns_response(response_data)
    print(f"Received DNS response (Transaction ID: {transaction_id}) from server - IP Address: {ip_address} For domain Name: {domain_name}")

    client_socket.close()

if __name__ == "__main__":
    main()
