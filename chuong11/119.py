def party_check(arrivals,name):
    index = arrivals.index(name)
    if index<len(arrivals)/2 and index != len(arrivals)-1:
        return True
    return False
arrivals = ['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
name_check = 'Adela'
result = party_check(arrivals,name_check)
print(result)
