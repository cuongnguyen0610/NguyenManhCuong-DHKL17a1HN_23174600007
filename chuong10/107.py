s=['a','b','c','d','e','f','duck']
print(s[3])
print(s[0:])
####
find = "duck" in s
print(find)
print(s[6])
####
for i in range(len(s)):
    if s[i]=="d":
        s[i]="dog"
    print(s[i], end=" ")    
### 
print(s.count(3))    