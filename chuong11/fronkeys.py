list1 = ["one","two","three","four"]
dict1 = dict.fromkeys(list1)
print(dict1)
dict1 = dict.fromkeys(list1,[12,33,44,5])
print(dict1)
#####
dic_animals = {1:"elephant",2:"dog",3:"duck",4:"bear",5:"ant"}
print(dic_animals.get(3))
### Ví dụ 11.69
d = {1:'one',2:'two',3:'three'}
print('d.get(3)=',d.get(3))
print("d[3] =",d[3])
d[4]='bon'
print(d)
### Trả về các value của dictionary
dic_animals = {1:"elephant",2:"dog",3:"duck",4:"bear",5:"ant"}
print(dic_animals.items())
####
print(dic_animals.values())
###Cập nhật dictionary bằng cách thêm dictionary khác vào
dic_nums = {1:'one',2:'two',3:'three'}
dic_added = {4:'four',5:'five'}
dic_nums.update(dic_added)
print(dic_nums)
#Duyệt dictionary
d = {1:'one',2:'two',3:'three',4:'four'}
for i in d:
    print(i,end=" ")
    ###
for i in d.keys():
    print(i,end=" ")
    ###
for i in d.items():
    print(i,end=" ")
    ###
for i in d.values():
    print(i,end=" ")
                


