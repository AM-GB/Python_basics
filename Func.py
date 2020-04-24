
def pr_sep(sep = '-', sep_val = 100):
    return sep * sep_val

def hello_max(who):
    print('Hello', who)

def greeting(who, say = 'Hello'):
    print(say, who)

def greetings(say, *args): #при * получаем кортеж
    print(say, args)

def get_person(**kwargs): #при ** получаем словарь
    for k,v in kwargs.items():
        print(k, v)

print(pr_sep('-', 100))
print(pr_sep('*', 100))

hello_max('Max')
print(pr_sep('-', 100))

greeting('Hi', 'Leo')
greeting(say='Hi', who='Leo')
greeting('Max')

print(pr_sep())
greetings('Hello', 'leo')
greetings('Hello', 'leo', 'Dan')
greetings('Hello', 'leo', 'Max', 'kot')

print(pr_sep())
get_person(name='Leo', age=20, has_car=True)


