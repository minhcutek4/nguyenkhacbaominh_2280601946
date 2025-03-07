def chia_het_5(nhi_phan):
    so_thap_phan = int(nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
    

str = input("Nhập các số nhị phân: ")
tach = str.split(',')
so_chia_5 = [so for so in tach if chia_het_5(so)]
if len(so_chia_5) > 0:
    ketqua = ','.join(so_chia_5)
    print("Các số chia hết cho 5 là: ", ketqua)
else:
    print("Không có số nào chia hết cho 5")
