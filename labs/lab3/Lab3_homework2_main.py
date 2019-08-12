"""
Домашняя работа 3, задание 2
Задание наследование и полиморфизм
 Вариант 9

"""
import datetime
import labs.lab3.Lab3_homework2_def as inventory

# создать список объектов product
inventory_items = [
     inventory.Flowers("Гвоздики", 1.20, "Красные", 40),
     inventory.Flowers("Розы", 2.50, "Красные", 40),
     inventory.Flowers("Розы", 2.60, "Красные", 50),
     inventory.Clock("Casio", 203.80, "Цифровые"),
     inventory.Clock("Луч", 130, "Аналоговые"),
     inventory.Clock("Xiaomi", 83, "Аналоговые"),
     inventory.Cake("Киевский", 12.20, 1.0, datetime.date(2019, 8, 16), 670),
     inventory.Cake("Сказка", 11.50, 0.8, datetime.date(2019, 9, 11), 620),
     inventory.Candy("Аленка", 11.50, "Шоколад", datetime.date(2019, 8, 10), 720),
     inventory.Candy("Пчелки", 6.20, "Мармелад", datetime.date(2019, 10, 20), 560)
 ]


# Подсчет стоимость всех товаров
total_sum = 0
for i in range(len(inventory_items)):
    total_sum += inventory_items[i].get_price()

print("Стоимость всех товаров: " + str(total_sum) + "р")
print("---------------------------")


bestbefore_limit = datetime.date(2019, 8, 20)
print("Список товаров со сроком годности до " + str(bestbefore_limit))
print("=================================")

for i in range(len(inventory_items)):
    if isinstance(inventory_items[i], inventory.Food):
        if inventory_items[i].get_bestbefore() < bestbefore_limit:
            print(inventory_items[i].get_name() + "(" + str(inventory_items[i].get_bestbefore()) + ")")
print("---------------------------------")

