import math
def giai_phuong_trinh_bac_2(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                return "Phương trình vô số nghiệm"
            else:
                return "Phương trình vô nghiệm "
        else: 
            return "Phương trình có một nghiệm duy nhất"
    else:
        delta = b**2 - 4*a*c
        if delta <0:
            return "Phương trình vô nghiệm"        
        elif (delta==0): 
            return "Phương Trình có nghiệm kép",-b/c      
        else:
            return  (-b + math.sqrt(delta)/(2*a)), (-b - math.sqrt(delta)/(2*a))
a ,b ,c = map(int, input("Nhập vào 3 biến:").split())  
print(giai_phuong_trinh_bac_2(a,b,c))
 
                
           