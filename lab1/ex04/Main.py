from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU**********************")
    print("** 1. Thêm sinh viên.                             **")
    print("** 2. Cập nhật thông tin sinh viên bởi id.        **")
    print("** 3. Xóa sinh viên bởi id.                       **")
    print("** 4. Tìm kiếm sinh viên theo tên.                **")
    print("** 5. Sắp xếp sinh viên theo điểm trung bình.     **")
    print("** 6. Sắp xếp sinh viên theo tên.                 **")  # Fixed menu description
    print("** 7. Hiển thị danh sách sinh viên.               **")
    print("** 0. Thoát.                                      **")
    print ("***************************************************")
    key = int(input("Nhập tùy chọn: "))
    
    if (key == 1):
        print("\n1.Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
        
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2.Cập nhật thông tin sinh viên.")
            print("Nhập ID : ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên rỗng.")
            
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3.Xóa sinh viên.")
            print("\nNhập ID : ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh vien co id =", ID, "da bi xoa.")
            else:
                 print("\nSinh vien co id =", ID, "khong ton tai.")
        else:
            print("Danh sách sinh viên rỗng.")
            
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4.Tìm kiếm sinh viên theo tên.")
            print("\nNhập tên sinh viên cần tìm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên rỗng.")
            
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5.Sắp xếp sinh viên theo điểm trung bình.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên rỗng.")
            
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6.Sắp xếp sinh viên theo tên.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên rỗng.")
            
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7.Hiển thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên rỗng.")
            
    elif (key == 0):
        print("bạn đã chọn thoát chương trình này.")
        break
    else:
        print("\nKhông có chức năng này.")
        print("\nHãy chọn chức năng trong menu.")