a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
if a>b:
    a=a-b
    print(f"{a} là ước chung lớn nhất")
elif a==b:
    print(f"{a} là ước chung lớn nhất")
else:
    b=b-a
    print(f"{b} là ước chung lớn nhất")


