import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64) # 64 bytes = 512 bits
    blake2_hash.update(message)
    return blake2_hash.digest()

def main():
    text = input("Nhap chuoi can bam: ").encode('utf-8')
    hash_value = blake2(text)
    
    print("Chuoi van ban da nhap la:", text.decode('utf-8'))
    print("BLAKE2 hash:", hash_value.hex())
    
if __name__ == "__main__":
    main()