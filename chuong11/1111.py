tuple = ('red','green','yellow','blue','black','white','pink','orange','red','blue')
n = int(input(" Nhập index dương từ 0<=index<10"))
m = int(input(" Nhập index dương từ -1<=index<-9"))
print(tuple[n])
print(tuple[m])
find = 'blue'
appear = tuple.count(find)
print(f"blue xuất hiện {appear} lần")