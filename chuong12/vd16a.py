#var1 ở trong không gian tên global namespace
var1 =5
def some_func():
    var2=6
    #var2 trong khoong gian tên cục bộ (local namespace)
    print("giá trị của biến var2 trong không gian tên local namespace (hàm some_func) là:",var2)
    def some_inner_func():
        #var3 trong không gian cục bộ lồng nhau (nested local namespace)
        var3=7
        print("Giá trị của biến var3 trong không gian tên nested local namespace (hàm some_inner_func) là",var3)
    some_inner_func()   # Gọi hàm some_inner_func() từ trong hàm some_func()
print("Giá trị của biến var trong không gian tên global namespace là:",var1)
some_func()

##3#
# var is in the global namespace
var = 5
def some_func():
# var is in the local namespace
    var = 6
    print("giá trị biến var2 trong local hàm some_func là : ",var)
    def some_inner_func():
#var3 is in the nested local namespace #
        var = 7
        print("Giá trị biến var3 trong nested local namespace là: ", var)
    some_inner_func()
print("giá tri biến var trong không gian global namespace là: ", var)
some_func()
print("Giá trị biến var sau khi gọi hàm some_func() là ", var)
        