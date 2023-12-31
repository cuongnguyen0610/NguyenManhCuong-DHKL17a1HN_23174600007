#Xây dựng hàm module.py
import math
def bmi(can_nang,chieu_cao):
    BMI = can_nang/math.pow(chieu_cao,2)
    print(BMI)
    return BMI
w= int(input("nn:"))
h = int(input("mm:"))
bmi(w, h)
