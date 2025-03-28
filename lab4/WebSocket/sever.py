import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketSever(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        WebSocketSever.clients.add(self)
        
    def on_close(self):
        WebSocketSever.clients.remove(self)
    
    @classmethod
    def send_message(cls, message : str):
        print(f"Sending message: {message}")
        for client in cls.clients:
            client.write_message(message)

class randomwordselector:
    def __init__(self, words):
        self.words = words
    
    def sample(self):
        return random.choice(self.words)
    
def main():
    app = tornado.web.Application(
        [(r"/websocket", WebSocketSever)], 
        WebSocketSever_ping_interval=10, 
        WebSocketSever_ping_timeout=30,
    )
    app.listen(8888)
    
    io_loop = tornado.ioloop.IOLoop.current()
    
    word_selector = randomwordselector(["hello", "world", "tornado", "websocket"])
    
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketSever.send_message(word_selector.sample()), 3000
    )
    periodic_callback.start()
    
    io_loop.start()
    
if __name__ == "__main__":
    main()