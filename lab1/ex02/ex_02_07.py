print("Nhập văn bản (nhập 'done' để kết thúc): ")
a = []
while True:
    m = input()
    if m.lower() == 'done':
        break
    a.append(m)
print("kết quả: ")
for m in a:
    print(m.upper())
    