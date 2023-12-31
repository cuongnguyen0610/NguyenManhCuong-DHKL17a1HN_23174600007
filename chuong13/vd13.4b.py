f = open('bai_tho.txt', 'r' , encoding = 'utf-8')
a= f.readline()
print('Nội dung dòng đầu là:', a)

b = f.readline()
print('Nội dung dòng 2 là:', b)

c=f.readline()
print('Nội dung dòng 3 là:',c)

d=f.readline()
print('Nội dung dòng 4 là:',d)

f.close()