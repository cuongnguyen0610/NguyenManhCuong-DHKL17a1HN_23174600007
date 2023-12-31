a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
x,y = a,b
while x!=y:
 if (x>y):
    x=x-y
 elif x==y:
    print("ước chung lớn nhất là:",x)
 else:
    y=y-x   
print("bội chung nhỏ nhất của ",a," và ",b, "là:",(a*b/x))     
