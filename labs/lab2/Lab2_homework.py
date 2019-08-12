"""
Домашнее задание 2-
Сортировка
"""
import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

# сортировка вставками Insert
def InsertSort (A):
   for i in range(len(A)):
       t = A[i]
       j = i
       while j != 0:
           if A[j-1] > t:
               A[j] = A[j-1]
               j -= 1
           else:
               break
       A[j] = t

# шейкерная сортировка
def ShakerSort(A):
   for i in range(len(A) // 2):
       for j in range(i, len(A) - 1 - i):
           if A[j] > A[j + 1]:
               A[j], A[j + 1] = A[j + 1], A[j]
       for j in range(len(A) - 2 - i, i + 1, -1):
           if A[j] < A[j - 1]:
               A[j], A[j - 1] = A[j - 1], A[j]

table = prettytable.PrettyTable(["Размер списка", "Время вставкой","Время шейкерной"])
x=[]
y1=[]
y2=[]

for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    B=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    B = A.copy()

    t1 = datetime.datetime.now()
    InsertSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Cортировка вставками " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    ShakerSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Шейкерная сортировка " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()



