#một số ví dụ tham chiếu liên kết dữ liệu chuẩn và list
x=5
y=x
x=3
y
print(x is y)
#Kiểu dữ liệu dạng List và xlist và ylist
xlist=[1,2]
ylist=xlist
xlist[0]=10
print(ylist)
print(xlist is ylist)