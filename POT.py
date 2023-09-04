import socket
import threading
import datetime

# Define the honeypot port
HONEYPOT_PORT = 22  # Change to the desired port

# Function to handle incoming connections
def handle_connection(client_socket):
    client_address = client_socket.getpeername()
    print(f"[*] Accepted connection from: {client_address[0]}:{client_address[1]}")

    # Log the connection to a file
    with open("honeypot.log", "a") as log_file:
        log_file.write(f"[{datetime.datetime.now()}] Connection from: {client_address[0]}:{client_address[1]}\n")

    # Close the client socket
    client_socket.close()

# Function to start the honeypot
def start_honeypot():
    # Create a server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", HONEYPOT_PORT))
    server.listen(5)

    print(f"[*] Honeypot listening on 0.0.0.0:{HONEYPOT_PORT}")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_connection, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_honeypot()
