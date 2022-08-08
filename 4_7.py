import my_input
import math


def fact(num):
    for i in range(1, num + 1):
        yield math.factorial(i)


n = my_input.int_pos_input()
for el in fact(n):
    print(el)
