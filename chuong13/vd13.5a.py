#Ví dụ về con trỏ tập tin , hàm tell(),hàm seek()
f = open('bai_tho.txt',"r+")
a = f.read(12) #đọc 12 kí hiệu đầu tiên
print("nội dung 12 ký tự đầu tiên là:", a)

b = f.tell()  #Kiểm tra vị trí hiện thời của con troe tập tin
print("Vị trí hiện thời của con trỏ tập tin :", b)

f.seek(0)   # Dặt lại con trỏ về vị trí đầu file
c = f.read(12)
print('Các ký tự được sau khi trở về vị trí ở dàu file là', c)
