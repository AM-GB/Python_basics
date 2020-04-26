import random

numbers = [random.randint(-100, 100) for i in range(15)]
print(numbers)

result = [number for number in numbers if number > 0 and number %3 == 0 and number %4 != 0]\

print(result)
