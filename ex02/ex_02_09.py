def check_snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("Nhập số: "))

if check_snt(number):
    print(number, "là số nguyên tố")
else:
    print(number, "không phải là số nguyên tố")