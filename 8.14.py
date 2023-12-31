n = int(input("Nhập n lần số nguyên"))
tong=0
for i in range(n):
    so_nguyen= int(input(f"Nhập số nguyên thứ {i+1}"))
    tong+=so_nguyen
    print(tong)