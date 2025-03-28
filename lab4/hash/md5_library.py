import hashlib

def caculate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("nhap chuoi can bam: ")
md5_hash = caculate_md5(input_string)

print("MD5 hash '{}' la : {}".format(input_string, md5_hash))