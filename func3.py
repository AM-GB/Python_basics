def f():
    print('hello from other f')

def to(f_param):
    # параметром будет функция
    f_param()

to(f)