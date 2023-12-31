f = open('bai_tho.txt', 'r' , encoding = 'utf-8')
a= f.read(25)
print('Nội dung 25 ký tự đầu là:',a)

b = f.read(35)
print('Nội dung 35 ký tự tiếp theo là:',b)

c=f.read()
print('Nội dung còn lại là:',c)

f.close()