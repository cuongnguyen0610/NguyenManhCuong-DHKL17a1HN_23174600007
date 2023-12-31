dic_animals = {1:"elephant",2:"dog",3:"duck",4:"bear",5:"ant"}
print("Before:",dic_animals)
dic_animals_copy = dic_animals.copy()
print("create of copy a dictionary:",dic_animals_copy)
######
tu_dien_thu_cung = {1:'Chim hoa mi',2:'Ca ba duoi',3:'Ran',4:'Tran',5:'Ky Nhong',6:'Ca Ong tien'}
ban_sao = tu_dien_thu_cung.copy()
print("Copy:",ban_sao)
for i in ban_sao:
    ban_sao[i]=ban_sao[i].upper()
    print(i, ':', ban_sao[i])
    
    print("\nBan goc:")
    for i in tu_dien_thu_cung:
        print(i,':',tu_dien_thu_cung[i])
        
    