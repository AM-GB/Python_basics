# ДЗ № 3
import random

def get_random(input_list):
    if input_list: # будет True если список не пустой
        result = random.choice(input_list) #выбирает случайный элемент из списка
        return result

if __name__ == '__main__':
    n = [1, 3, 7, 9, 8]

    print(get_random(n))
    print(get_random([]))