import re

def calculate_sum():
    # Nhập chuỗi từ bàn phím
    string = input("Nhập chuỗi: ")

    # Tìm và trích xuất tất cả các số từ chuỗi
    numbers = re.findall(r"-?\d+", string)

    # Khởi tạo biến tổng
    positive_sum = 0
    negative_sum = 0

    # Tính tổng cho từng số
    for number in numbers:
        number = int(number)
        if number > 0:
            positive_sum += number
        elif number < 0:
            negative_sum += number

    # In kết quả
    print("Giá trị dương:", positive_sum)
    print("Giá trị âm:", negative_sum)

# Gọi hàm calculate_sum để chạy chương trình
calculate_sum()