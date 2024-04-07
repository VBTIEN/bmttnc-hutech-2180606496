import itertools

def print_permutations(lst):
    permutations = list(itertools.permutations(lst))
    for permutation in permutations:
        print(permutation)

# Gọi hàm print_permutations với danh sách [1, 2, 3]
print_permutations([1, 2, 3])