#Cú pháp 1 : newlist = [expression for item in list]
#Ví dụ 11.25: tạo list mới là các phần tử chữ HOA
fruits = ['apple','banana','cherry','kiwi','mango']
newlist = [x.upper() for x in fruits]
print(newlist)
## 1 cách khác
fruits = ['apple','banana','cherry','kiwi','mango']
for i in range(len(fruits)):
	fruits[i]=fruits[i].upper()
print(fruits)
### Cú pháp 2
### newlist = [expression for item in list if condition ==True]
fruits = ['apple','banana','cherry','kiwi','mango']
newlist = [x if x!= "banana" else "orange" for x in fruits]
print(newlist)
###c2
fruits = ['apple','banana','cherry','kiwi','mango']
for i in range(len(fruits)):
	if fruits[i]=="banana":
		fruits[i]="orange"
print(fruits)		


