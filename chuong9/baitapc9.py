#9.
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

# Test phương thức với một số ví dụ
print(sign(5))    # Kết quả: 1 (số dương)
print(sign(-3))   # Kết quả: -1 (số âm)
print(sign(0))    # kết quả :0 (số 0)
#9.2
def nam_am_lich(nam_duong_lich):
    # Lấy phần dư khi chia cho 10 để xác định can
    can_index = nam_duong_lich % 10

    # Lấy phần dư khi chia cho 12 để xác định chi
    chi_index = nam_duong_lich % 12

    # Xác định can
    if can_index == 0:
        can = 'Canh'
    elif can_index == 1:
        can = 'Tân'
    elif can_index == 2:
        can = 'Nhâm'
    elif can_index == 3:
        can = 'Quý'
    elif can_index == 4:
        can = 'Giáp'
    elif can_index == 5:
        can = 'Ất'
    elif can_index == 6:
        can = 'Bính'
    elif can_index == 7:
        can = 'Đinh'
    elif can_index == 8:
        can = 'Mậu'
    else:
        can = 'Kỷ'

    # Xác định chi
    if chi_index == 0:
        chi = 'Thân'
    elif chi_index == 1:
        chi = 'Dậu'
    elif chi_index == 2:
        chi = 'Tuất'
    elif chi_index == 3:
        chi = 'Hợi'
    elif chi_index == 4:
        chi = 'Tý'
    elif chi_index == 5:
        chi = 'Sửu'
    elif chi_index == 6:
        chi = 'Dần'
    elif chi_index == 7:
        chi = 'Mão'
    elif chi_index == 8:
        chi = 'Thìn'
    elif chi_index == 9:
        chi = 'Tỵ'
    elif chi_index == 10:
        chi = 'Ngọ'
    else:
        chi = 'Mùi'

    return f'{can} {chi}'

# Nhập năm dương lịch từ người dùng
nam_duong_lich = int(input("Nhập năm dương lịch: "))

# Gọi hàm và in kết quả
nam_am = nam_am_lich(nam_duong_lich)
print(f"Năm âm lịch tương ứng là: {nam_am}")
####9.3
import math
def so_bmi(can_nang,chieu_cao):
    chi_so_bmi= can_nang/(math.pow(chieu_cao,2))
    if chi_so_bmi <18.5:
        print("gầy:",chi_so_bmi)
    elif 18.5<=chi_so_bmi<=24.99:
        print("bình thường:",chi_so_bmi)  
    else:
        print("béo:",chi_so_bmi)      
    return chi_so_bmi
can_nang = float(input("cân nặng:"))
chieu_cao = float(input("chiều cao:"))   
so_bmi(can_nang,chieu_cao)
####9.4
import math

s = lambda x,y:math.pow(math.pow(x,2)+1,y)
print(s(2,3))
####9.5
import math
s1 =lambda x,y:(x**2 + x + 1)**y + (x**2 - x + 1)**y
import math

A = lambda x, n: math.pow(x**2 + x + 1, n) + math.pow(x**2 - x + 1, n)
print(s1(3,4))
print(A(5,6))
#####9.6
def so_nguyen_to(n):
    if n<0:
        print("vui lòng nhập số nguyên dương")
    elif n<2:
        print(f"{n} không phải số nguyên tố")
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                False
            break   
        else:
            True  
    return n
so_nguyen_to(7)    
#####9.7
def phan_nguyen_phep_chia(a,b):
    return a//b
a = int(input("Nhập a"))
b = int(input("Nhập b"))
ket_qua= phan_nguyen_phep_chia(a,b)
print("phần nguyên phép chia:",ket_qua)
######9.8
def so_hoan_hao(n):
    if n<0:
        print("Vui lòng nhập lại số dương")
    else:
        tonguoc =0
        for i in range(1,n//2+1):
            if n%i==0:
                tonguoc+=i
        if n==tonguoc:
            print(f"{n} là số hoàn hảo")
        else:
            print(f"{n} không phải là số hoàn hảo")
    return n

n = int(input("Nhập n:"))
hoan_hao = so_hoan_hao(n)
#baitap 9.9
import math


s = lambda r: math.pi*math.pow(r,2)
s1 = lambda r: 2*math.pi*r
print(s(5))
print(s1(7))
###
s2=lambda a,b: a*b 
print(s2(2,3))








