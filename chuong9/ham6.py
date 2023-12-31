#Variable-length argument
#use asterisks(*) when parameter change
#There is only one parameter of this type in function
#parameters of this type must
def in_loi_chao(loi_chao,*danh_sach_ten):
    #In tên theo danh sách tên
    for ten in danh_sach_ten:
        print(loi_chao,ten)
    return
#in_loi_chao("Hello")
in_loi_chao("Hello","lan","Mai","Truc","Dao")