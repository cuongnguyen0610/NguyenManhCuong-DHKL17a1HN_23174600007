x = int(input("Nhập số tiền bạn muốn đổi:"))
if (x>=500000):
    print("số tờ 500000 là:",x//500000)
    x%=500000
if (x>=200000):
    print("số tờ 200000 là:",x//200000)
    x%=200000
if (x>=100000):
    print("số tờ 100000 là:",x//100000)
    x%=100000    
if (x>=50000):
    print("số tờ 50000 là:",x//50000)
    x%=50000
if (x>=20000):
    print("số tờ 20000 là:",x//20000)
    x%=20000  
if (x>=10000):
    print("số tờ 10000 là:",x//10000)
    x%=10000   
else:
    print("số tiền còn lại là:",x)           