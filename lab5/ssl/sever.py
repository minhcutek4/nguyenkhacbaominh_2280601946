import socket
import ssl
import threading

sever_address = ('localhost', 12345)

clients = []

def handle_client(client_socket):
    clients.append(client_socket)
    print("Da ket noi voi: ", client_socket.getpeername())
    
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Nhan:", data.decode('utf-8'))
            
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)
    except:
        clients.remove(client_socket)
    finally:
        print("Ngat ket noi: ", client_socket.getpeername())
        clients.remove(client_socket)
        client_socket.close()
        
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_socket.bind(sever_address)
sever_socket.listen(5)

print("Dang cho ket noi...")

while True:
    client_socket, client_address = sever_socket.accept()
    
    #tao ssl context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(certfile="./certificates/server-cert.crt", 
                            keyfile="./certificates/server-key.key")
    ssl_socket = context.wrap_socket(client_socket, server_side=True)
    
    client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
    client_thread.start()