# nums = [5, 7, 2, 4, 7, True, "Hello", 6.7,[5,6]] #prosto spisok []
# # print(nums)

# # nums[0] = True
# # print(nums)
# # print(nums[-1][1]) # Выводим последний элемент основного списка и последний элемент вложенного

# a = {}
# print(type(a))     # <class 'dict'>

# b = {1, 2, 3}   
# print(type(b))     # <class 'set'>

# c = {'a': 1, 'b': 2}
# print(type(c))     # <class 'dict'>

# # Зададим исходно список и словарь (скопировать перед примерами ниже):
# my_list = ['a', 'b', 'c', 'd', 'e', 'f']
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# print(my_list)   # ['a', 'b', 'c', 'd', 'e', 'f']
# print(my_dict)   # {'a': 1, 'c': 3, 'e': 5, 'f': 6, 'b': 2, 'd': 4}

# 2.2 Подсчёт количества членов коллекции с помощью функции len()

# print(len(my_list)) # 6
# print(len(my_dict)) # 6 - для словаря пара ключ-значение считаются одним элементом. 
# # print(len('ab c')) # 4 - для строки элементом является 1 символ

# 2.3 Проверка принадлежности элемента данной коллекции c помощью оператора in

# x in s — вернет True, если элемент входит в коллекцию s и False — если не входит
# Есть и вариант проверки не принадлежности: x not in s, где есть по сути, просто добавляется отрицание перед булевым значением предыдущего выражения.

# my_list = ['a', 'b', 'c', 'd', 'e', 'f']
# print('a' in my_list)           # True
# print('q' in my_list)           # False
# print('a' not in my_list)       # False
# print('q' not in my_list)       # True

# Для словаря возможны варианты, понятные из кода ниже:

# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# print('a' in my_dict)               # True - без указания метода поиск по ключам
# print('a' in my_dict.keys())        # True - аналогично примеру выше
# print('a' in my_dict.values())      # False - так как 'а' — ключ, не значение
# print(1 in my_dict.values())        # True

# Можно ли проверять пары? Можно!

# print(('a',1) in my_dict.items())   # True
# print(('a',2) in my_dict.items())   # False

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print('a' in my_dict)               # True - без указания метода поиск по ключам
print('a' in my_dict.keys())        # True - аналогично примеру выше
print('a' in my_dict.values())      # False - так как 'а' — ключ, не значение
print(1 in my_dict.values())        # True