#đọc tập tin height.txt là tập tin chứa dữ liệu về chiều cao vận động viên, sau đó tính chiều cao trung bình theo mét
f = open('heights.txt')
data = f.read()   #Biến data là một biến kiểu chuỗi ký tự
f.close()

#Xử lý dữ liệu đọc từ file 'heights.txt'
#Bước 1. Chuyển đổi sang list ,  phần tử kiểu chuỗi Ký tự 
lst = data.split(",")

#Bước 2. Tạo một danh sách heights là các phần tử kiểu số thực
height = [float(item) for item in lst]

#Bước 3 . Dổi đơn vị đo chiều cao sang mét
height_m = [h*0.0254 for h in height]

#Bước 4. tính chiều cao trung bình các vđv
mean = sum(height_m)/len(height_m)
print("Chiều cao trung bình của vdv :",mean)
