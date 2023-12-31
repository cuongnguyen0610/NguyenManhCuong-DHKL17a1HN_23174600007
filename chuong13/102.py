def read_report_file(filename):
    try:
        with open(filename,"r",encoding='utf-8') as f:
            content =f.read()
            lines=content.split('\n')
            word=content.split()
            
            num_lines = len(lines)
            num_word = len(word)
            num_chars=len(content)
            
            print("Nội dung tập tin:")
            print(content)
            print(f"Số dòng: {num_lines}")
            print(f"Số từ: {num_words}")
            print(f"Số ký tự: {num_chars}")
    except FileNotFoundError:
        print("Không tìm thấy tập tin!!!!")
read_report_file("HumptyDumty.txt")        
            
            