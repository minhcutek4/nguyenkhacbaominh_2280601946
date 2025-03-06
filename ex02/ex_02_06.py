nhap_mang = input("Nhap X, Y: ")
kich_thuoc = [int(i) for i in nhap_mang.split(",")]
X = kich_thuoc[0]
Y = kich_thuoc[1]
m = [[0 for j in range(Y)] for i in range(X)]
for i in range(X):
    for j in range(Y):
        m[i][j] = i*j
print(m)