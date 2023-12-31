def value_zip_code(zip_code):
    if len(zip_code) == 6 and zip_code.isdigit():
        return True
    else:
        return False
zip_input = input("Nhập mã zip vào :")
result = value_zip_code(zip_input)
if result:
    print(f"{zip_input} là mã zip code việt nam")
else:
    print(f"{zip_input} không phải zip code việt nam")      