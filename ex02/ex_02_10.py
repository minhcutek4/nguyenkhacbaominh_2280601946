def dao_nguoc(chuoi):
    return chuoi[::-1]

nhap_chuoi = input("Nhập chuỗi: ")
print(dao_nguoc(nhap_chuoi))