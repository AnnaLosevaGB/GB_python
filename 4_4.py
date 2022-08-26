first_list = [10, 2, 1, 3, 16, 10, 10, 23, 154, 2, 45, 16, 23, 10, 2, 18, 31, 16, 345]
my_dict = {k: first_list.count(k) for k in first_list}
print([key for key, value in my_dict.items() if value == 1])
