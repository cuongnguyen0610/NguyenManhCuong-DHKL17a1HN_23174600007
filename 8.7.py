so_kwh = int(input("Nhập vào số kwh:"))
if so_kwh <= 50:
    tien_dien = so_kwh*1678
elif so_kwh <=100:
    tien_dien = 50*1678 + so_kwh*1734
elif so_kwh <=200:
    tien_dien = 50*1678 + 50 * 1734 +so_kwh*2014
elif so_kwh <=300:
    tien_dien =  50*1678 + 50 * 1734 +100*2014 +so_kwh*2536
elif so_kwh <=400:   
    tien_dien =  50*1678 + 50 * 1734 +100*2014 +100*2536 +so_kwh*2834
else:
    tien_dien =  50*1678 + 50 * 1734 +100*2014 +100*2536 +100*2834+(so_kwh-400)*2927
print("tổng tiền điện của gia đình bạn:",tien_dien)                 
gia_phong = {"Standard":1260000,
              "Superior Garden View":1550000,
              "Superior Ocean View":1830000,
              "Garden View Bungalow":1830000,
              "Pool View Bungalow":2120000,
              "Family Room":2120000,
              "Beach Front Bungalow":2540000,
              "VIP sea View":4800000,
            }