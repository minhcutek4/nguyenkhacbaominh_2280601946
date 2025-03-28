import socket
import ssl
import threading

sever_address = ('localhost', 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhan:", data.decode('utf-8'))
    except:
        pass
    finally:
        ssl_socket.close()
        print("Ngat ket noi voi sever")
        
#tao socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#tao ssl context
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False

#thiet lap ket noi ssl
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

ssl_socket.connect(sever_address)

#nhan du lieu tu sever
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

#gui du lieu den sever
try:
    while True:
        message = input("Nhap tin nhan: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    ssl_socket.close()
    