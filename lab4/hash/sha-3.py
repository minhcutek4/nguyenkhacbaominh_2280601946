from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhap chuoi can bam: ").encode('utf-8')
    hash_value = sha3(text)
    
    print("Chuoi van ban da nhap la:", text.decode('utf-8'))
    print("SHA3-256 hash:", hash_value.hex())
    
if __name__ == "__main__":
    main()