# Задача 1 Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9,
# ответ: 12

import random

list_size = int(input("Введите размер списка: "))
list = []
sum = 0
for i in range(list_size):
    list.append(random.randint(0, 100))
    if i % 2 != 0:
        sum += list[i]

print(list)
print(sum)


