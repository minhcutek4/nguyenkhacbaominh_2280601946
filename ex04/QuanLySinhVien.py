from SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien = []
    
    def generateId(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
       svId = self.generateId()
       name = input("Nhập tên sinh viên: ")
       sex = input("Nhập giới tính: ")
       major = input("Nhập ngành học: ")
       diemTB = float(input("Nhập điểm trung bình: "))
       sv = SinhVien(svId, name, sex, major, diemTB)
       self.xepLoaiHocLuc(sv)
       self.listSinhVien.append(sv) 

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính: ")
            major = input("Nhập ngành học: ")
            diemTB = float(input("Nhập điểm trung bình: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên co ID = {} không tồn tại.".format(ID))
            
    def sortByID(self):
                self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
                
    def sortByName(self):
                self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
                
    def sortByDiemTB(self):
                self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True)
                
    def findByID(self, ID):
        searchResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(sv._id == ID):
                    searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv: SinhVien):
        if(sv._diemTB >= 8):
            sv._hocLuc = "giỏi"
        elif(sv._diemTB >= 6.5):
            sv._hocLuc = "khá"
        elif(sv._diemTB >= 5):
            sv._hocLuc = "trung bình"
        else:
            sv._hocLuc = "yếu"
            
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "name",'sex', "major", "Diem TB", "Học lực"))
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name,sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")
        
    def getListSinhVien(self):
        return self.listSinhVien    