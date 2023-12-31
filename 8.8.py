loai_phong = int(input("Nhập loại phòng:"))
so_dem = int(input("nhập số đêm:"))
gia_phong = {
    1: 1260000,
    2: 1550000,
    3: 1830000,
    4: 1830000,
    5: 2120000,
    6: 2120000,
    7: 2540000,
    8: 4800000
}
if loai_phong in gia_phong:
 gia_1_dem = gia_phong[loai_phong]
 if so_dem == 1:
   tien_thue_phong = gia_1_dem
 elif so_dem == 2 or so_dem == 3:
  tien_thue_phong = gia_1_dem*so_dem*0.75
 else:
  tien_thue_phong = gia_1_dem*so_dem*0.7
 print(f"số tiền bạn phải trả {tien_thue_phong}") 
else:
 print("căn phòng không hợp lí")  
