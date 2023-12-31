def menu_is_boring(meals):
    for i in range(len(meals)-1):
        if meals[i]==meals[i+1]:
            return True
    return False
meal_1 = ['Redneck Ribs','Prawn Star','San Quentin Squid','Fist Full of Pizza','Honky Tonk Chicken']
meal_2 = ['Redneck Ribs','Prawn Star','Running bear Salmon','Running bear Salmon','Honky Tonk Chicken']
result = menu_is_boring(meal_1)   
results = menu_is_boring(meal_2)
print(result)
print(results) 