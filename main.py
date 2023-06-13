# Задача 30. Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# l_size = int(input("enter list size"))
# first_el = int(input("enter first num"))
# dif_el = int(input("enter diff"))
# print(list_1 := [x:=(first_el + (dif_el * i)) for i in range(l_size)])

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

l_size = int(input("enter list size"))

print(list_1 := [random.randint(0, 20) for _ in range(l_size)])

l_max = int(input("enter max"))
l_min = int(input("enter min"))

print(list_ind := [i for i in range(len(list_1)) if list_1[i] >= l_min and list_1[i]<= l_max])