import socket
import sys


class Client:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._socket = socket.socket()
        self.connect()

    def connect(self) -> None:
        try:
            print(f"client: connecting to server at {self._host}:{self._port}")
            self._socket.connect((self._host, self._port))
            print(f"client: successfully connected to server")
        except Exception as e:
            raise Exception(f"client: Failed to connect to server at {self._host}:{self._port}: {e}")

    def send_message(self, data: bytes) -> bytes | None:
        try:
            print(f"client: sending message {data}")
            count = self._socket.send(data)
            print(f"client: sent {count} bytes of data")
        except Exception as e:
            print(f"client: failed to send message {data}: {e}")
        try:
            print(f"client: waiting for server response")
            return self._socket.recv(1024)
        except Exception as e:
            print(f"client: failed to receive response: {e}")

    def close(self) -> None:
        try:
            self._socket.close()
            print("client: connection closed")
        except Exception as e:
            print(f"client: failed to close connection: {e}")


if __name__ == "__main__":
    client_name = sys.argv[1] if len(sys.argv) > 1 else "default"
    print(f"client: starting client {client_name}")
    client = Client("localhost", 9999)
    messages = [b"This is the first message", b"This is the second message", b"This is the third message",
                b"This is the fourth message"]
    for message in messages:
        resp = client.send_message(message)
        print(f"client: received response {resp}")
    client.close()
