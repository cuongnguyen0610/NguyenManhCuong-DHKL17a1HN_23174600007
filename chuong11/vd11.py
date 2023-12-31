all_list = ['one','abc','two','three','abc',1,2,3]
print(all_list.index("abc"))
###
lst = [1,3,4,5,6,7,8,9]
lst_max= []
for i in lst:
    if i==max(lst):
        continue
    else:
        lst.append(i)
print("Giá trị lớn thứ hai :",max(lst_max))
lst_index=[]
for j in range(len(lst)):
    if lst[j]==max(lst_max):
        lst_index.append(j)
print(lst_index)        
