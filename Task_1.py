# Напишите программу, которая принимает на вход два числа
# и проверяет - является ли одно квадратом другого
a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))

if a == b**2:
    print('Your first number is a square of the second number')
elif b == a**2:
    print('Your second number is a square of the first number')
else:
    print('One of the numbers is not a square of the other number')