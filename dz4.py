def func():
    pass # пустая функция

def unlucky_number(number):
    if number == 13:
        raise ValueError('Не счасливое число')
    else:
        return number ** 2

number = int(input('Введите число: '))

try:
    result = unlucky_number(number)
except ValueError:
    print('У нас не счасливое число')
else:
    print(result)