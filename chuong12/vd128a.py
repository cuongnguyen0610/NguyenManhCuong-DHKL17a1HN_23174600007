#Chuong trình minh họa phạm vi của đối tượng
def some_func():
    print("bên trong hầm some_func:")
    def some_inner_func():
        var=10
        print("Bên trong hàm some_inner_func() , giá trị của var là:",var)
    some_inner_func() #Gọi hàm some_inner_func() từ trong hàm some_func()
    print("Try printing var  outer function: ",var)   
some_func() 