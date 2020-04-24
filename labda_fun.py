# применяются для создания анонимных функций по месту их использования
# lambda входные параметры: результат
def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(my_filter(numbers, lambda number: number % 2 == 0))
print(my_filter(numbers, lambda number: number % 2 == 1))
print(my_filter(numbers, lambda number: number > 4))
