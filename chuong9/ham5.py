import math
def tinh_bmi(can_nang,chieu_cao):
    bmi = can_nang/math.pow(chieu_cao,2)
    return bmi
bmi = tinh_bmi(52,1.6)
print("BMI:",bmi)
#Tham số mặc định(Default argument)
def choose_drink(price,drink="coffee"):
    print("with",price,"vnd, you can buy",drink)
    return
choose_drink(10000,"tea")
    