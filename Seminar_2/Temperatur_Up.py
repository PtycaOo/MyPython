n = int(input("Количество дней: "))
x = int(input("Введите первую температуру: "))
count = 0
for i in range(n - 1):
    y = int(input("Введите температуру: "))
    if y > x:
        count += 1
    x = y
    

print(count)