"""
Домашняя работа 3, задание 2
Задание наследование и полиморфизм
 Вариант 9

"""
from datetime import date


# Класс Продукт
class Product:
    # наименовение
    __name: str = ""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# Класс Товар
class Goods(Product):
    # Стоимость
    __price = 0

    def __init__(self, name, price):
        Product.__init__(self, name)
        self.__price = price

    def get_price(self):
        return self.__price


class Flowers(Goods):
    # Длина
    __length = 0
    # Цвет
    __color = ""

    def __init__(self, name, price, color, length):
        Goods.__init__(self, name, price)
        self.__color = color
        self.__length = length

    def get_length(self):
        return self.__length

    def get_color(self):
        return self.__color


class Clock(Product):
    # Тип часов
    __type = ""

    def __init__(self, name, price, type):
        Goods.__init__(self, name, price)
        self.__type = type


# Класс пищевые товары
class Food(Goods):
    # Срок годности
    __bestbefore = date.today()
    # Калорийность
    __energy = 0

    def __init__(self, name, price, bestbefore, energy):
        Goods.__init__(self, name, price)
        self.__energy = energy
        self.__bestBefore = bestbefore

    def get_energy(self):
        return self.__energy

    def get_bestbefore(self):
        return self.__bestbefore


# Класс Торты
class Cake(Food):
    # Масса
    __weight = 0

    def __init__(self, name, price, weight, bestbefore, energy):
        Food.__init__(self, name, price, bestbefore, energy)
        self.__weight = weight

    def get_weight(self):
        return self.__weight


class Candy(Food):
    # Начинка
    __filling = ""

    def __init__(self, name, price, filling, bestbefore, energy):
        Food.__init__(self, name, price, bestbefore, energy)
        self.__filling = filling

    def get_filling(self):
        return self.__filling
