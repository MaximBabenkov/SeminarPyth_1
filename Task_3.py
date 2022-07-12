# Напишите программу, которая  на вход будет принимать
# число N и выводить числа от -N до N
n = int(input('Enter your number: '))
min = -n

while min <= n:
    print(min, end=' ')
    min += 1
