"""
Домашняя работа 4, задание 1
Вариант 2
Скопировать в файл F2 только те строки из F1,  которые начинаются с буквы «А». Подсчитать количество слов в F2.
"""
import os

print("Content of the F1 file:\n")
try:
    with open("F1.txt") as file_F1:
        for line in file_F1:
            print(line)
except IOError:
    print("An IOError has occurred!")

# Скопировать в файл F2 только те строки из F1,  которые начинаются с буквы «А».
try:
    with open("F1.txt", "r") as F1:
        with open("F2.txt", "w") as F2:
            lines = F1.readlines()
            for i in lines:
                if i[0] == "A":
                    F2.write(str(i))
except FileNotFoundError:
    print("File F1 does not exist!")

# Подсчитать количество слов в F2
try:
    word_count = 0
    with open("F2.txt", "r") as F2:
            for line in F2:
                word_count += len(line.split())
except FileNotFoundError:
    print("File F2 does not exist!")

print("number of words in F2 : ", word_count)