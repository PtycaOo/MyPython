from random import randint
count = 0
max_Value = 0
row_bushes = 0
number_of_bushes = int(input("Введите количество кустов "))
lst = []
for i in range(number_of_bushes):
    lst.append(randint(1,10))

print(lst)

for x in lst:
    row_bushes+=1
    for i in range(3):
        count+=lst[i]
    if count > max_Value:
        max_Value = count
    
    lst = lst[1:]+lst[:1]
    print(f"Количество ягод с кустов № {row_bushes} = {count}")
    count = 0

print(f"Максимальное количество ягод {max_Value}")
        



