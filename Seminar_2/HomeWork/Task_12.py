S = abs(int(input('Введите первое натуральное число S ')))
P = abs(int(input('Введите второе натуральное число P ')))
y = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
x = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(x, "  ", y)