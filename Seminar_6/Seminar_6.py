# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# # print(*find_farthest_orbit(orbits))
# # Вывод:
# # 2.5 10

# def find_farthest_orbit(orbits):
#     condition = lambda data: (data[0] != data[1]) * data[0] * data[1]
#     square_orbits = list(map(condition, orbits))
#     return orbits[square_orbits.index(max(square_orbits))]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# # отличается - то False. Для пустого набора объектов, функция
# # должна возвращать True. Аргумент characteristic - это
# # функция, которая принимает объект и вычисляет его
# # характеристику.



# def same_by(characteristic,object):
#     return len(set(map(characteristic,object))) in (0,1)

# values = [0, 2, 10, 6]

# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")

