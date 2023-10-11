# # num_row = int(input("Введите количество рядом: "))
# # num_columns = int(input("Введите количество столбцов: "))
# def print_operation_table(operation, num_rows , num_columns ):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         print(' '.join([str(i) for i in range(1, num_columns + 1)]))
#         for i in range(2,num_rows+1):
#             print(i, end = " ")
#             for j in range(2,num_columns+1):
#                 print(operation(i,j), end = " ")
#             print()


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# list_r = [print(i) for i  in range(len(list_1)) if min_number <= list_1[i] <= max_number]

list_1 = [1,2,4,5,14,18]
def res(x,y):
    if x < y:
        return x
    
print(list(filter(res(2,4),list_1)))