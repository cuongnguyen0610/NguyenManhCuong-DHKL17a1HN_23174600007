dic_animals = {1:"elephant",2:"dog",3:"duck",4:"bear",5:"ant"}
print("Before:",dic_animals)
del dic_animals[1]
print("after:",dic_animals)
dic_animals.clear()
print("After remove all:",dic_animals)
del dic_animals
print("After deleted dic:",dic_animals)