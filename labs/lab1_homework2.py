"""
Домашнее задание 1-
Задание 2 Вариант № 3
"""
import math

a = 6
y = -1.55
for_j = [8, -0.6, 1, 6.4]

print("Исходные данные: ")
print("a=" + str(a))
print("y=" + str(y))

print("for : ")
for j in for_j:
    z = math.sqrt(a+1) - math.tan(j + y)
    q = math.exp(-j * 0.1 * y) + (3 * z)**2
    print("z = " + str(z) + " q = " + str(q) + " for j = " + str(j))

print("while : ")
j = -1
while j <= 1:
    z = math.sqrt(a + 1) - math.tan(j + y)
    q = math.exp(-j * 0.1 * y) + (3 * z) ** 2
    print("z = " + str(z) + " q = " + str(q) + " for j = " + str(j))
    j += 0.2

print("double :")
a = 1
for_j = [3.3, -4, 0.9]
while a <= 2 :
    for j in for_j:
        z = math.sqrt(a + 1) - math.tan(j + y)
        q = math.exp(-j * 0.1 * y) + (3 * z) ** 2
        print("z = " + str(z) + " q = " + str(q) + " for a = " + str(a) + " for j = " + str(j))
    a += 0.2







