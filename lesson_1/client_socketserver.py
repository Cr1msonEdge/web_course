import socket, sys

address_to_server = ("localhost", 8686)


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(address_to_server)
        
        data = input("enter message: ")
        sock.sendall(bytes(data, "UTF-8"))

        received = str(sock.recv(1024), "UTF-8")
        print(f"Was sent: {data}")
        print(f"Was recieved: {received}")


