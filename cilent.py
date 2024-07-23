import socket

def client(host='192.168.0.137', port=9999):
    """Connect to the server and send a single message ack."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send("Hello, Server!".encode('utf-8'))
    response = client.recv(4096).decode('utf-8')
    print(f"Received: {response}")
    client.close()

if __name__ == "__main__":
    client()