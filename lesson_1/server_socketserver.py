import socketserver


class TCPHandler(socketserver.BaseRequestHandler):
    # обработчик запросов для сервера

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} sent message:")
        data = self.data.decode("UTF-8")
        print(data)
        self.request.sendall((data + " - was returned").encode("UTF-8"))


SERVER_ADDRESS = ("localhost", 8686)

print("Server is started.")

with socketserver.TCPServer(SERVER_ADDRESS, TCPHandler) as serv:
    serv.serve_forever()
