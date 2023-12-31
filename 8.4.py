import math
a =  float(input("Nhập giá trị a:"))
b =  float(input("Nhập giá trị b:"))
c =  float(input("Nhập giá trị c:"))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"Diện tích tam giác là {S}")