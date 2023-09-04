import socket
import threading

def handle_client(client_socket):
    # Connect to the remote server
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect(("www.example.com", 80))  # Change to the target server and port

    while True:
        # Receive data from the client
        client_data = client_socket.recv(4096)
        if not client_data:
            break

        # Forward data to the remote server
        remote_socket.send(client_data)

        # Receive data from the remote server
        remote_data = remote_socket.recv(4096)
        if not remote_data:
            break

        # Forward data to the client
        client_socket.send(remote_data)

    client_socket.close()
    remote_socket.close()

def main():
    # Create a server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))  # Listen on all network interfaces on port 8080
    server.listen(5)  # Allow up to 5 queued client connections

    print("[*] Listening on 0.0.0.0:8080")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
