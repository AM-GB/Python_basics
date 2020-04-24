def some_f():
    return 10

result = some_f()
print(result)

a = some_f #функция тоже объект и ее можно присваивать переменной
print(a)

print(type(a))

print(a())
