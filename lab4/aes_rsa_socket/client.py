from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

#initialize client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

#generate RSA key pair
client_key = RSA.generate(2048)

#receive server's public key
server_public_key = RSA.import_key(client_socket.recv(2048))

#send client's public key to server
client_socket.send(client_key.publickey().export_key(format='PEM'))

#receive encrypted AES key from server
encrypted_aes_key = client_socket.recv(2048)

#decrypt AES key with client's private key
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

#function to encrypt message
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ct

#function to decrypt message
def decrypt_message(key, encrypted_message):
    iv = encrypt_message[:AES.block_size]
    ct = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypt_message = unpad(cipher.decrypt(ct), AES.block_size)
    return decrypt_message.decode()

#funtion to received mess from server
def received_messages():
    while True:
        encrypt_message = client_socket.recv(1024)
        decrypted_message = decrypt_message(aes_key, encrypt_message)
        print("Received:", decrypted_message)
    
#start the receiving thread
received_thread = threading.Thread(target=received_messages)
received_thread.start()

#send mess from the client
while True:
    mess = input("enter mess ('exit to quit): ")
    encrypted_message = encrypt_message(aes_key, mess)
    client_socket.send(encrypted_message)
    if mess == "exit":
        break
    
#close
client_socket.close()
