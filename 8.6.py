khoang_cach= float(input("Nhập vào số km:"))
loai_xe = int(input("Nhập vào loại xe:"))
time_cho = int(input("thời gian chờ là:"))
if loai_xe == 4:
  gia_mo_cua = 11000
  khoang_cach_dau = 0.8
  trong_pham_vi_20km = 12100
  gia_km_thu_21_tro_di = 10000
  gia_tri_sau_5p_dau_mien_phi = 800
  max_km_dau = 21
if loai_xe == 7:
  gia_mo_cua == 13000
  khoang_cach_dau = 0.8
  trong_pham_vi_30km = 14100
  gia_km_thu_31_tro_di = 12000
  gia_tri_sau_5p_dau_mien_phi = 800
  max_km_dau=31
gia_taxi = 0
if khoang_cach <= khoang_cach_dau:
  gia_taxi = gia_mo_cua  
elif khoang_cach <= max_km_dau :
  if loai_xe ==4:
   gia_taxi = gia_mo_cua + (khoang_cach - khoang_cach_dau)*trong_pham_vi_20km  
  else:
   gia_taxi = gia_mo_cua + (khoang_cach - khoang_cach_dau)*trong_pham_vi_30km
else:
  if loai_xe ==4:
    gia_taxi = gia_mo_cua + (khoang_cach - khoang_cach_dau)*gia_km_thu_21_tro_di
  else:
    gia_taxi = gia_mo_cua + (khoang_cach - khoang_cach_dau)*gia_km_thu_31_tro_di


tien_cho = 0
if time_cho > 5:
  tien_cho = gia_tri_sau_5p_dau_mien_phi *(time_cho-5)
print("tiền cước là :",gia_taxi + tien_cho)      


   




