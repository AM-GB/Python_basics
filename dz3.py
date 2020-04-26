import math
import random

old_list = [random.randint(-9, 9) for i in range(15)]
print(old_list)


def new_sqrt_list(input_list):
    input_list = input_list.copy() #copy позволяет не менять old_list
    for i in range(len(input_list)):
        number = input_list[i]
        if number > 0:
            input_list[i] = math.sqrt(number)

    return input_list

def new_sqrt_list_True(input_list):
    # комбинация тернарного оператора и генератораы
    result = [math.sqrt(number) if number > 0 else number for number in input_list]
    return result

result = new_sqrt_list(old_list)
print(result)
result = new_sqrt_list_True(old_list)
print(result)
print(old_list)


