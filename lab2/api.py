from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayfairCipher
app = Flask(__name__)

caesar_cipher = CaesarCipher()
@app.route('/api/Caesar/encrypt', methods=['POST'])

def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_mess': encrypted_text})

@app.route('/api/Caesar/decrypt', methods=['POST'])

def caesar_decrypt():
    data = request.json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_mess': decrypted_text})

vigenere_cipher = VigenereCipher()
@app.route('/api/Vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_mess': encrypted_text})

@app.route('/api/Vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_mess': decrypted_text})



playfair_cipher = PlayfairCipher()
@app.route('/api/Playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

@app.route('/api/Playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_mess': encrypted_text})

@app.route('/api/Playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_mess': decrypted_text})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)