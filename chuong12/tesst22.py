#vd12.1
import math
def tinh_bmi(can_nang,chieu_cao):
    bmi = can_nang/math.pow(chieu_cao,2)
    return bmi
#vd 12.2
import my_module
#Gọi hàm trong my_module
print(my_module.tinh_bmi(52,1.6))
#Ví dụ 12.3
#module tính toán hai số
import math
def tong(x,y):
    return x+y
def hieu(x,y):
    return x-y
##Ví dụ 12.4
import tinh_toan_hai_so
x,y=3,5
print()

###Vị trí lưu trữ module

