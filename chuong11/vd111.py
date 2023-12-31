fruits = ['apple','banana','cherry','kiwi','mango']
for i in range(len(fruits)):
 fruits[i]=fruits[i].upper()
print(fruits) 
##
fruits = ['apple','banana','cherry','kiwi','mango']
newlist = [x for x in fruits if "a" in x]
print(newlist)
###
fruits = ['apple','banana','cherry','kiwi','mango']
newlist1 = [x if x!= "banana" else "orange" for x in fruits]
print(newlist1)
