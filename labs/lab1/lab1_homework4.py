"""
Домашнее задание 1-
Задание 4 Вариант № 4
"""
import random

n = int(input("Введите размер списка: "))
L = []
for i in range(n):
    l = random.randint(0,999)
    L.append(l)
print("Элементы списка: ")
print(L)
minimum = L[0]
for j in range(1, len(L)):
    if L[j] < minimum:
        minimum = L[j]
print("Минимальный элемент списка = " + str(minimum))