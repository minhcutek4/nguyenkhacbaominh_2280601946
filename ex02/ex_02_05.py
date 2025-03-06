so_gio_lam = float(input("Nhập số giờ làm: "))
luong_theo_gio = float(input("Nhập lương theo giờ: "))
gio_tieu_chuan = 44
gio_tang_ca = max(0, so_gio_lam - gio_tieu_chuan)
luong = gio_tieu_chuan * luong_theo_gio + gio_tang_ca * luong_theo_gio * 1.5
print(f"Lương của bạn là", luong)