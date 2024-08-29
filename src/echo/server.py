import socket


class Server:

    def __init__(self, host: str = "localhost", port: int = 9999):
        self._host = host
        self._port = port
        self.socket = socket.socket()
        self.socket.bind((self._host, self._port))
        self.socket.listen()
        print(f"server: start listening on {self._host}:{self._port}")

    def accept(self) -> None:
        while True:
            connection, client_address = self.socket.accept()
            print(f"server: new connection established from {client_address}")
            while True:
                message = connection.recv(1024)
                if len(message) == 0:
                    print(f"server: connection closed by client {client_address}")
                    connection.close()
                    break
                else:
                    print(f"server: received message {message}")
                    print(f"server: echoing message back to client")
                    connection.send(message)


if __name__ == "__main__":
    server = Server()
    try:
        server.accept()
    except KeyboardInterrupt:
        server.socket.close()
        print(f"server: stopped due to keyboard interrupt")
