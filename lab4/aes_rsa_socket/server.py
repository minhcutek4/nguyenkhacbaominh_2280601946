from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

#initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

#generate RSA key pair
server_key = RSA.generate(2048)

#list of connected clients
clients = []

#function to encrypt message
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message, AES.block_size))
    iv = cipher.iv
    return iv + ct_bytes

#function to decrypt message
def decrypt_message(ciphertext, key):
    iv = encrypt_message[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypt_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypt_message.decode()

#function to handle client
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    
    #send server's public key to client
    client_socket.send(server_key.publickey().export_key(format='PEM'))
    
    #receive client's public key
    client_received_key = RSA.import_key(client_socket.recv(2048))



    #genarate AES key for message encryption
    aes_key = get_random_bytes(16)

    #encrypt AES key with client's public key
    cipher_rsa = PKCS1_OAEP.new(client_received_key)
    encrypt_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypt_aes_key)

    #add client to list of connected clients
    clients.append((client_socket, aes_key))
    
    while True:
        encrypt_message = client_socket.recv(1024)
        decrypt_message = decrypt_message(encrypt_message, aes_key)
        print(f"Message from {client_address}: {decrypt_message}")
        
        #send received mess to all other client
        for client, key in clients:
            if client != client_socket:
                encrypt = encrypt_message(decrypt_message, key)
                client.send(encrypt)
                
        if decrypt_message == "exit":
            break
    
    clients.remove((client_socket, aes_key))
    client_socket.close()
    print(f"Connection from {client_address} closed")
    
#accecpt and handle client connection
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
    