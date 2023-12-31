f = open('bai_tho.txt', 'r' , encoding = 'utf-8')
a= f.readline()
print('Nội dung dòng đầu là:', a)

b = f.readlines()
print('Nội dung các dòng còn lại là: \n', b)

c=f.readlines()
print('Nội dung các dòng còn lại là: \n',c)



f.close()