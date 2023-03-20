# # Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

N = int(input('ddd: '))
k =1
result = 2
while result <= N:
    if k< 2:
        result *= k
        k +=1
    else:
        k = 2
        result *= k
    if result<N:
        print(result, end=', ')
