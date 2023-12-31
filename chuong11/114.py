x = []
n = int(input("Nhập giá trị list:"))
for i in range(0,n):
    x.append(int(input(f"Nhập phần tử thứ {i+1}:")))
   # tiep_tuc=input("Tiếp tục nhập giá trị? 1: Có , 0: Không")
    #if tiep_tuc =="0":
    #    break
print("list nums =", x)    
sum =0 
for y in x:
    sum+=y
print("total=",sum)    
print("2 xuất hiện ",x.count(2),"trong list")
lon_hon_5 = []
for so in x:
    if so >= 5:
        lon_hon_5.append(so)
print(lon_hon_5)        
    