# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint

count = int(input('Введите количество монет: '))
reshka =0
orel =0
for _ in range(count):
    coins = randint(0, 1)
    print(coins, end=' ')
    if coins == 0:
        reshka +=1
    else:
        orel +=1
print()
if reshka>orel:
    print (orel)
else:
    print(reshka)
