import random

n = int(input("Колличество монет "))
mas = []
count_zero=0
count_one=0
for i in range(n):
    mas.append(random.randint(0, 1))
    if mas[i] == 0:
        count_zero+=1 
    else:
        count_one+=1
print("Монеты на столе ", mas)   
if count_zero > count_one:
    print(count_one)
else :
    print(count_zero)