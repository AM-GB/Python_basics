numbers = [1, 5, 3, 5, 9, 7, 11]
print(sorted(numbers))
# сортировка по убыванию
print(sorted(numbers, reverse=True))

# набор строк
names = ['Max', 'Alex', 'Kate']
# сортировка по алфавиту
print(sorted(names))

cities = [ ('Москва', 1000), ('Лас-Вегас', 500), ('Антверпен', 2000)]
# такая сортировка сработает поалфавиту
print(sorted(cities))
#сортировка по на населению

def by_count(city):
    return city[1]

print(sorted(cities, key=by_count))
print(sorted(cities, key=lambda c: c[1]))