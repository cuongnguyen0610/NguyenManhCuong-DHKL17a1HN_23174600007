n=int(input("mời nhập vào số năm:"))

if ((n%4==0 and n%100!=0) or n%400==0):
        print(f"{n} là năm nhuận")
else:
        print(f"{n} không pahri năm nhuận")          
