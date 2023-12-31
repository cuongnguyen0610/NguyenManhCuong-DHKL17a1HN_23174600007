#Tham trị
def tinh_binh_phuong(so):
    so=so*so
    print("Giá trị của số trong hàm:%d"%so)
    return
so=9
tinh_binh_phuong(so)
#Tham chiếu
def change_list(lst):
    #Thêm vào sau list
    lst.append(10)
    lst.append(20)
    print("list trong hàm:",lst)
    return
lst=[1,3,7,12]
print("list ban đầu",lst)
change_list(lst)