import math
def tinh_so_bmi(can_nang,chieu_cao):
    bmi = can_nang/math.pow(chieu_cao,2)
    print("chỉ số bmi:%0.2f"%bmi)
    return 
w=float(input("Nhập số cân nặng:"))
h=float(input("cho biết số đo chiều cao"))
tinh_so_bmi(w,h)

