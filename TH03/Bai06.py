def xoa_phan_tu(dictionnary, key):
    if key in dictionnary:
        del dictionnary[key]
        return True
    else:
        return False
# sử dụng hàm và in kết quả
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = xoa_phan_tu(my_dict , key_to_delete)
if result:
    print("phần tử đã được xóa từ Dictionary : ", my_dict)
else:
    print("Không tìm thấy phần tử đã được xóa từ Dictionary. ")