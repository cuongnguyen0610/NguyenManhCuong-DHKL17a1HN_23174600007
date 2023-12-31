list = [74,74,72,72,73,69,69,71,76,71]
quy_doi = 0.0254
inch= []
for i in list:
    inch.append(i*quy_doi)
print(inch)    
# In ra 3 chiều cao đầu tiên
print("3 chiều cao đầu tiên:", list[:3])

# In ra 3 chiều cao cuối cùng
print("3 chiều cao cuối cùng:", list[-3:])
## in ra chiều cao trung bình
tong = sum(list)
dai = len(list)
tbc=tong/dai
print("Trung bình cộng",tbc)
# sắp xếp list
list.sort()
list.reverse()
print(list)
