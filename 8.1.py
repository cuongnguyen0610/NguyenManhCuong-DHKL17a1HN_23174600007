a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=int(input("Nhập c:"))
d=int(input("Nhập d:"))
max =a
min =a
if b > max:
    max =b
if b < min:
    min =b
if c> max:
    max =c
if c<min:
    min=c
if d>max:
    max=d
if d<min:
    min=d
print(f"số lớn nhất là {max}")
print(f"số lớn nhất là {min}")                        