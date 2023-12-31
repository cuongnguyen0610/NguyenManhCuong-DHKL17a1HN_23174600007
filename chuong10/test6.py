def binpow(a, b):
    if b==0:
        return 1
    #ditinh (a^b/2)
    X = binpow(a, b//2)
    if b%2==0:
        return X*X
    else:
        return X*X*a 
a, b=map(int,input().split())   
print(binpow(a, b)) 
###
def S(n):
    if n==0:
        return 0
    else:
        return 1/n+S(n-1)
n=int(input())
print(S(n))
######
def F(n):
    if n!=0:
        F(n//2)
        print(n%2, end ='')
n=int(input())
print(F(n))
            