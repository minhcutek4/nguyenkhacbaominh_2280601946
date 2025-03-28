import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        self.connect_and_read()

    def stop(self):
        self.io_loop.stop()

    def connect_and_read(self):
        print("Reading...")

        future = tornado.websocket.websocket_connect(
            "ws://localhost:8888/websocket"
        )

        future.add_done_callback(self.maybe_retry_connect)

    def maybe_retry_connect(self, future):
        try:
            self.connection = future.result()
            print("Connected to WebSocket server")
            self.connection.read_message(self.on_message)
        except Exception as e:
            print(f"Connection failed: {e}, retrying in 3 seconds...")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, message):
        if message is None:
            print("Disconnected, reconnecting...")
            self.connect_and_read()
            return

        print(f"Received message: {message}")
        self.connection.read_message(self.on_message)

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    
    io_loop.add_callback(client.start)
    io_loop.start()

if __name__ == "__main__":
    main()
