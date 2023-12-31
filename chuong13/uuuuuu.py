my_dict = {'apple':1,'banana':2,'cherry':3}
result = 'banana' in my_dict.keys()
print(result)
###
a= [1,2,3,4,5]
b=a 
b[2]=10
result = a[2]
print(result)
#### 
u = (1,2,[3,4])
u[2][0]=30
rr=u 
print(u)
####
a = {1,2,3}
b = {3,4,5}
i = a.intersection(b)
print(i)
####
r = {'a':1,'b':2,'c':3}
o = list(r.keys())
x = 'c' in o
print(x)
###
v = [0,1,2,3,4,5,6]
lst = v[::2]
print(lst)
### 
numbers = [1,2,3,4,5]
results = list(map(lambda x: x*2 , numbers))
print(results)