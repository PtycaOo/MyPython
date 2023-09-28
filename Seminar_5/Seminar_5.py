# # # Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# # # Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# # Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# # # Ввод: 					Вывод:
# # # 7					ответ: 3 3 2 12
# # # 3 1 3 4 2 4 12
# # # 6
# # # 4 15 43 1 15 1

# n = int(input("Введите элементы первого списка: "))
# list_1 = [int(i) for i in input("Введите элементы массива через пробел: ").split()[:n]]
# m = int(input("ВВедите элементы второго списка: "))
# list_2 = [int(i) for i in input("Введите элементы массива через пробел: ").split()[:m]]

# # print(*[i for i in list_1 if i not in  list_2])


# n = int(input("Введите кол-во элементов списка: "))
# first_list = [int(i) for i in input("Введите значения списка: ").split()[:n]]
# # 12 35 8 9 1
# print(sum([first_list[i - 1] < first_list[i] > first_list[i + 1]
#            for i in range(1, n - 1)]))



# numbers = [int(i) for i in input("Введите значения списка: ").split()]
# count_numbers = {}
# for i in numbers:
#     if i not in count_numbers:
#         count_numbers[i] = 1
#     else:
#         count_numbers[i]+=1

# print(count_numbers)
# print(sum([i // 2 for i in count_numbers.values()]))


n = int(input("Input number: "))
data = {}
for i in range(2, n + 1):
    summa = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            summa += j
    data[i] = summa
print_list = list()
for k, v in data.items():
    if v in data.keys() and k in data.values() and k != v and data[v] == k and data[k] == v\
            and (k, v) not in print_list:
        print(k, v)
        print_list.append((v, k))