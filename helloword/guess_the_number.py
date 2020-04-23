#Загадать случайное число +
import random

number = random.randint(1, 100)
print(number)

# Предложить пользователю ввести число
#user_nuber = int(input('Введите число: '))
#print(user_nuber)

user_nuber = None
count = 0
levels = {1: 10, 2: 5, 3: 3} #блокнот

level = int(input('Введите уровень сложности: '))
max_count = levels[level]

user_count = int(input('Введите количество пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i+1}: ')
    users.append(user_name)

print(users)

winner_name = None
is_winner = False

while number != user_nuber:
    count += 1
    if count > max_count:
        print('Все проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        user_nuber = int(input('Введите число: '))
        if user_nuber == number:
            is is_winner = True
            winner_name = user
            break
        #Сравнение чисел
        elif number < user_nuber:
            print('Ваше число больше чем загаданное')
        else:
            print('Ваше число меньше чем загаданное')
else:
    print(f'Победитель {winner_name}')
