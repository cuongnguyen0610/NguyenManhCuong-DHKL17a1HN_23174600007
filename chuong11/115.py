x = []
n = int(input("Nhập giá trị list:"))
for i in range(0,n):
    x.append(int(input(f"Nhập phần tử thứ {i+1}:")))
    tiep_tuc=input("Tiếp tục nhập giá trị? 1: Có , 0: Không")
    if tiep_tuc =="0":
        break
print("list nums =", x)  
def la_so_nguyen_to(nt):
    if nt<2:
        return False
    else:
        for i in range(2,(int(nt**0.5)+1)):
            if nt%i==0:
                return False
        return True     
so_nguyen_to = list(filter(la_so_nguyen_to,x))
so_nguyen_to = []
for so in x:
    if la_so_nguyen_to(so):
        so_nguyen_to.append(so)
print("số nguyên tố trong 1 list là =",so_nguyen_to)       
## Các phần tử âm trong list
so_am = []

for so in x:
    if so < 0:
        so_am.append(so)

# In ra danh sách các số âm
print("Các số âm trong danh sách:", so_am)   
### trung bình cộng
tong=0
for r in so_am:
    tong+=r
    tbc = tong/len(so_am)
    print("Trung bình cộng là:",tbc)
## Các phần tử dương trong list
so_duong = []

for so in x:
    if so > 0:
        so_duong.append(so)

# In ra danh sách các số âm
print("Các số duong trong danh sách:", so_duong)   
##tbc dương
tong = sum(so_duong)
dai = len(so_duong)
tbc = tong/dai
print("Trung bình cộng số dương:",tbc)
### tìm giá trị lớn nhất nhỏ nhất trong list
gia_tri_lon_nhat = max(x)
gia_tri_nho_nhat = min(x)    
print("Giá trị lớn nhất",gia_tri_lon_nhat)
print("Giá trị nhỏ nhất",gia_tri_nho_nhat)
#list sắp tăng dần
x.sort()
print(x)
      
                