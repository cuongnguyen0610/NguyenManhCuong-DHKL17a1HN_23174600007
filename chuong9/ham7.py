#Lambda,Map,Filter và Reduce
import math 
s= lambda x,n:math.pow(math.pow(x,2)+1,n)
print(s(2,3))
###
def bieu_thuc(x,n):
    s = math.pow(math.pow(x,2)+1,n)
    return s
bieu_thuc(2,3)
print(bieu_thuc(2,3))
#### lambda danh sách
corexplore = lambda x,y,z : x-y+z
print(corexplore(8,4,5))
####
coodinate =  [(4,7),(2,7),(-3,8),(5,-7)]
print(sorted(coodinate, key = lambda point : point[1]))
print(sorted(coodinate))
#####
number_list = [3,8,5,-3.-8,6,-6,2,0,1]
print(sorted(number_list))
print(sorted(number_list , key = lambda x: abs(x)))
#### 
def binh_phuong(x):
   s=x*x
   return s
List1 = [1,2,3,4,5]
list2 = list(map(binh_phuong,List1))
print(list2)
#####
list2 = list(map(lambda i:i**2,List1 ))
print(list2)
#Ví dụ 9.15
List1 = [1,2,3,4,5]
List2 = [6,7,8,9,10]
List4 = list(map(lambda i1,i2:i1+i2,List1,List2))
print(List4)
##### thư viện operator
from operator import add 
list_new = list(map(lambda i1,i2:i1+i2,[1,2,3,4,5],[2,3,4,5,6]))
print(list_new)
list_add = list(map(add,List1,List2))
print(list_add)
####Hàm Filter
list_number = [1,2,3,4,5,6,7,8,9,10]
list_even_number = list(filter(lambda i:i%2==0, list_number))
print(list_even_number)
####
list_string = ["abc","def","abf","stu","cba"]
list_string_a = list(filter(lambda i:"a" in i,list_string))
print(list_string_a)
print("list_filter",list(filter(lambda i:i=='a',"hello beaalalela")))
#Hàm reduce
#initialize:khởi tạo
from functools import reduce
from operator import add
list = [1,2,3,4,5]
sum1 = reduce(lambda x,y:x+y,list)
sum2 = reduce(add,list)
print(sum1)
print(sum2)
# Explain: mathemetically , it alike : f(f(f(f(f(x;y)y)y)y)y)
#ghép câu từ trong chuỗi list
list_word = ["he","has","a","cat"]
list = reduce(lambda x1,x2:x1+x2,list_word)
print(list)
#Tìm số lớn nhất trong List
num_list = [1,2,3,4,5]
max_num = reduce(lambda x,y:x if x>y else y , num_list)
print(max_num)
## 
list1 = [1,2,3,4,5,6,7,8,9]
max = list1[0]
for value in list1:
    if value > max:
        max = value
print(max)
###coordinate redude and filter to return factorial các số lẻ in the one list
from functools import reduce
list = [1,2,3,4,5]
tich_so_le = reduce(lambda x,y:x*y , filter(lambda x:x%2!=0 , list))
print(tich_so_le)
####vd 9.22
from functools import reduce
num_list = [1,2,3,4,5]
product_1 = reduce(lambda x,y:x*y,num_list)
print(product_1)
product_2 = reduce(lambda x,y:x*y,num_list,2)
print(product_2)
product_3 = reduce(lambda x,y:x*y,num_list,3)
print(product_3)
#######Built Function







