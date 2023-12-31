Alice = int(input("số kẹo của Alice là:"))
Bob = int(input("số kẹo của Bob là :"))
Carol = int(input("số kẹo của Carol là:"))
if (Alice,Bob,Carol>0):
    print("Số kẹo bạn nhập vào hợp lệ")
    All=Alice+Bob+Carol
    Candy_bi_du=All%3
    print(f"Số kẹo bị dư là:{Candy_bi_du}")
else:
    print("Mời bạn nhập lại số kẹo")    