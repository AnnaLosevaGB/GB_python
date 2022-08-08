first_list = [150, 0, 20, 30, 500, 16, 345, 345, 397, -5, 0, 28, 3]
print([first_list[i] for i in range(1, len(first_list)) if first_list[i] > first_list[i-1]])
