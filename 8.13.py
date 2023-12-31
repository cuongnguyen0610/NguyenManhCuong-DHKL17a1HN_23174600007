#Tổng các số lẻ nhỏ hơn hay bằng n
n = int(input(" nhập vào số nguyên n:"))
tong=0
for i in range(1,n+1,2):
    tong+=i
    print(tong) 
#Tổng các số chẵn  nhỏ hơn hoặc bằng n       
n = int(input(" nhập vào số nguyên n:"))
tong=0
for i in range(0,n+1,2):
    tong+=i
    print(tong) 
#tích các số từ 1 đến n    
n = int(input("nhập vào các số nguyên n:"))
tich =1
for i in range(1,n):
    tich*=i
    print(tich)
#tích các số chia hết cho 3 bé hơn hoặc bằng n
n = int(input(" nhập vào số nguyên n:"))
tich =1
for i in range(3,n+1,3):
    tich*=i
    print(tich)  
#tong cac so nguyen to be hon hoac bang n
import math
n = int(input("Nhập giá trị n:"))
tong =0
if n < 2:
    print("Đây không phải số nguyên tố:")
for i in range(2,int(math.sqrt(n)+1)):
    if n%i==0:
        print("Cũng không phải số nguyên tố")
        
    else:
        tong+=i
        print("Đây là số nguyên tố và tổng của nó là :",tong)
#tổng chuỗi đan dấu
n = int(input("Nhập số nguyên n: "))
tong = 0
chia = 1

for i in range(1, n + 1):
    if i % 2 == 1:
        tong += 1 / chia
    else:
        tong -= 1 / chia
    chia += 1

print("Tổng của chuỗi là:", tong)        

    


          
    



