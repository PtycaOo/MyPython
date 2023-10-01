num_row = int(input("Введите количество рядом: "))
num_columns = int(input("Введите количество столбцов: "))
for i in range(2,num_row+1):
    for j in range(num_columns):
        print(i, end = " ")
    print()