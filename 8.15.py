n = int(input("Nhập n lần số nguyên :"))
tong=0
for i in range(n):
    so_nguyen = int(input(f"Nhập 1 số nguyên lần thứ {i+1} ( kết thúc là số 0)"))
    if so_nguyen ==0:
        break
    tong+=so_nguyen
    print(tong)