def is_valid_zip_code(zip_code):
    # Kiểm tra độ dài chuỗi và xem tất cả các ký tự có phải là số không
    if len(zip_code) == 6 and zip_code.isdigit():
        return True
    else:
        return False

zip_input = input("Nhập mã zip code cần kiểm tra: ")
result = is_valid_zip_code(zip_input)

if result:
    print(f"{zip_input} là mã zip code hợp lệ của Việt Nam.")
else:
    print(f"{zip_input} không phải là mã zip code hợp lệ của Việt Nam.")