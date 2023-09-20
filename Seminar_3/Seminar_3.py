# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

# str1 = 'a a a b c a a d c d d'
# str1 = str1.split()
# my_dict = {}

# for i in str1:
#     if i not in my_dict:
#         my_dict[i] = 0
#         print(i, end = " ")
#     else:
#         my_dict[i] += 1
#         print(f'{i}_{my_dict[i]}', end=' ')

# str = '''She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure 
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells'''.lower()
# str = set(str.split())
# print(len(str))

# print(len(set(str.lower().split(' '))))


n = int(input("Введите число "))
max_number = -1
while n < 0:
   n = int(input("ВВедите число 2 "))
   if max_number < n:
       n = max_number
print(n)

n = int(input())
max_number = 1000
while n != 0:
   n = int(input())
   if max_number > n:
       max_number = n
print(max_number)