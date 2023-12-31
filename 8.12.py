import math
n = int(input("Nhập vào giá trị n:"))
if n<0:
    print("Vui lòng nhập lại số dương")
elif n<2:
    print(" không phải số nguyên tố")
else:
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            print(f"số {n} không phải số nguyên tố")
            break
    else:
        print(f"số {n} là số nguyên tố")    

