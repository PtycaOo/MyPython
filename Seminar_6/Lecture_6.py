# def summ(x):
#     return x * x

# # print(summ(5))

# # # создаем калькулятор

# def calk1(x,y):
#     return x+y

# def calk2(x,y):
#     return x*y

# def math(op,x,y):
#     print(op(x,y))


# math(lambda x,y: x+y,5,10)

# numbers = [1,2,3,5,8,15,23,38]
# numbers_final = []

# def list_double(my_list):
#     for i in my_list:
#         if i % 2 == 0:
#             numbers_final.append((i, i**2))
#     return numbers_final

# print(list_double(numbers))


def select(f,colection):
    return [f(x) for x in colection]

def where(f, colection):
    return [x for x in colection if f(x)]

numbers = [1,2,3,5,8,15,23,38]
numbers_final = select(int, numbers)
print(numbers_final)
numbers_final = where(lambda x: x % 2==0,numbers_final)
print(numbers_final)
numbers_final = select(lambda x: (x, x**2), numbers_final)
print(numbers_final)
