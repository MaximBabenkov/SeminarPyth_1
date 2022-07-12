# Напишите программу, которая на ввод принимает 5 чисел
# и находит максимальное из них
print('Enter your five numbers:')
a = []
for i in range(5):
    x = int(input())
    a.append(x)

max = a[0]
for i in range(1, len(a)):
    if a[i] > max:
        max = a[i]

print(f'Your maximum number: {max}')