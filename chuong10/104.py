import math
def S(x, n):
    
    s= math.pow(x**2+x+1,n)+math.pow(x**2-x+1,n)
    return s
n, k = map(int, input(" Nhập n , k").split()) 
print(S(n, k))