# A dictionary representing DNS records (hostname to IP address mapping)
dns_records = {
    "example.com": "192.168.1.100",
    "google.com": "8.8.8.8",
    "amazon.com": "176.32.103.205",
}

def resolve_dns(hostname):
    return dns_records.get(hostname, "Hostname not found")

if __name__ == "__main__":
    while True:
        hostname = input("Enter a hostname (or 'exit' to quit): ")
        if hostname.lower() == "exit":
            break
        ip_address = resolve_dns(hostname)
        print(f"{hostname} resolves to {ip_address}")
