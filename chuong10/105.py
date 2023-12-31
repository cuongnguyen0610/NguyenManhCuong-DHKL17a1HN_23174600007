import re

def is_valid_zip_code(zip_code):
    # Kiểm tra chuỗi có 6 chữ số và không chứa ký tự đặc biệt
    return bool(re.match(r'^\d{6}$', zip_code))

# Sử dụng hàm để kiểm tra mã zip code
zip_input = input("Nhập mã zip code cần kiểm tra: ")
result = is_valid_zip_code(zip_input)

if result:
    print(f"{zip_input} là mã zip code hợp lệ của Việt Nam.")
else:
    print(f"{zip_input} không phải là mã zip code hợp lệ của Việt Nam.")