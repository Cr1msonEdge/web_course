import socket
import threading
from random import randint

address_to_server = ("localhost", 8686)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address_to_server)


def read_messages(client_: socket.socket) -> None:
    while True:
        data = client_.recv(1024)
        print(data)
        if not data:
            break


thread = threading.Thread(target=read_messages, args=(client,))
thread.start()

# проверка на отправку большого сообщения
big_message = ''.join(chr(97 + randint(0, 25)) for _ in range(10000000))

while True:
    client.send(bytes(big_message + input("enter message: "), encoding="UTF-8"))


