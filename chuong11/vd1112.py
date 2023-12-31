list_nums = [10,55,8,12,7,9]
sum = 0
for num in list_nums:
 sum+=num
 print(sum) 
#Tính tổng và trung bình của list
ages = [23,25,22,24,23,26]
print('\n Ages:', ages)
sum =0 
for num in ages:
 sum+=num
print('Tổng',sum)
m = sum/len(ages)
print('Trung bình:', round(m,2))
### 
all_list = ['one','two','three','abc',1,2,3]
print(all_list.index("abc"))
###
fruits = ['apple','banana','cherry','kiwi','mango']
for i in range(len(fruits)):
 fruits[i]=fruits[i].upper()
print(fruits) 
###
i=0
while i <len(fruits):
 fruits[i]=fruits[i].upper()
 i+=1
print(fruits) 
##
fruits = ['apple','banana','cherry','kiwi','mango']
newlist = [x for x in fruits if "a" in x]
print(newlist)
### khác với trên
fruits = ['apple','banana','cherry','kiwi','mango']
for fruit in fruits:
 if 'a' in fruit:
  print(fruit)
# Ví dụ 11.27
fruits = ['apple','banana','cherry','kiwi','mango']
for i in range(len(fruits)):
    if fruits[i]=='banana':
        fruits[i]='orange'


print(fruits)
###
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# Duyệt từng phần tử trong danh sách
for i in range(len(fruits)):
    if fruits[i] == 'banana':
        fruits[i] = 'orange'

# In danh sách sau khi thay thế
print(fruits)
#Ghi nhớ
#Tạo list
#Duyệt list
#TRuy cập phần tử theo chỉ số
#thay đổi nội dung phần tử
#Cắt list
#Thêm phần tử vào list
#Bỏ phần tử ra khỏi list
#Tìm kiếm phần tử trong list
#sắp xếp các phần tử trong list
#List hỗn hợp

  



