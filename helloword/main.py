#Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке.
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].
#Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a \le ba≤b, c \le dc≤d.

a,b,c,d = int(input()),int(input()),int(input()),int(input())
st = ''
for i in range(a,(b+2)):
    if i == a:
        st += '\t'
    else:
        st += str(i-1) + '\t'
    for j in range(c,(d+1)):
        if i == a:
            st += str(j) + '\t'
        else:
            st += str((i-1)*j) + '\t'
    st += '\n'
print(st)
