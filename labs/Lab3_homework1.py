"""
Домашняя работа 3, задание 1 
Вариант 10
Создать класс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер.
Создать список объектов. Вывести:
a)	список автомобилей заданной марки;
b)	список автомобилей заданной модели, которые эксплуатируются больше n лет;
"""
from datetime import date
class Car:
     # id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер.
    __id = ""
    __marka = ""
    __model = ""
    __year = ""
    __colour = ""
    __price = 0
    __reg_num = ""

   # конструктор с присвоением заданных значений
   # id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер.
    def __init__(self, id, marka, model, year, colour, price, reg_num):
        self.__id = id
        self.__marka = marka
        self.__model = model
        self.__year = year
        self.__colour = colour
        self.__price = price
        self.__reg_num = reg_num

    # чтение id car
    def get_car_id(self):
        return self.__id

    # чтение марки car
    def get_car_marka(self):
        return self.__marka

    # чтение модели car
    def get_car_model(self):
        return self.__model

    # чтение года выпуска car
    def get_car_year(self):
        return self.__year

    # чтение цвета car
    def get_car_colour(self):
        return self.__colour

    # чтение цены car
    def get_price(self):
        return self.__price

    # чтение reg num car
    def get_reg_num(self):
        return self.__reg_num

    # получить возраст car
    def get_age_car(self):
        today = date.today()
        return today.year - self.__year

    # напечатать информацию об car
    def car_print_info(self):
        print(str(self.get_car_id()) + "   " +
              self.get_car_marka() + "   " +
              self.get_car_model() + "  " +
              str(self.get_car_year()) + "   " +
              self.get_car_colour() + "    " +
              str(self.get_price()) + "     " +
              self.get_reg_num()
              )
# main
# создать список объектов класса Car
Cars = [
   Car(1, "Opel", "Signum", 2005, "grey", 5400, "2304-MP 5"),
   Car(2, "Opel", "Astra", 2010, "white", 6400, "2504-MP 7"),
   Car(3, "Opel", "Vectra", 2003, "brown", 3700, "4304-SR 5"),
   Car(4, "VW", "Passat", 2013, "green", 10400, "8884-UI 5"),
   Car(5, "Audi", "A6", 2016, "grey", 15400, "5555-SP 7"),
   Car(6, "Audi", "A3", 2005, "red", 6400, "9304-AS 4"),
   Car(7, "Honda", "Civia", 2012, "yellow", 8800, "8904-DE 5"),
   Car(8, "Lada", "Vesta", 2018, "white", 13400, "7666-PP 7"),
   Car(9, "Lada", "Grada", 2016, "red", 10400, "2344-MP 3"),
   Car(10, "Audi", "A6", 2010, "red", 10500, "2255-AP 7")
]
print("Список всех автомобилей:")
print("Id  Marka  Model  Year   Colour Price   Reg_num ")
for i in range(len(Cars)):
    Cars[i].car_print_info()

# вывести список автомобилей заданной марки;
m = input("Введите марку автомобиля:")
count = 0
for i in range(len(Cars)):
    if str.capitalize(Cars[i].get_car_marka()) == str.capitalize(m):
       count += 1
if count == 0:
    m = print ("Такой марки нет в базе\n")

if count >0:
    print("Список всех автомобилей марки " + m + ":")
    print("Id   Marka   Model  Year   Colour    Price    Reg_num ")
    for i in range(len(Cars)):
        if str.capitalize(Cars[i].get_car_marka()) == str.capitalize(m):
            Cars[i].car_print_info()

# список автомобилей заданной модели, которые эксплуатируются больше n лет;
m = input("Введите модель автомобиля: \n")
n = int(input("Введите возраст автомобиля: \n"))
print("Список всех автомобилей модели " + str.capitalize(m) + " ,которые эксплуатируются больше " + str(n) + " лет:")
print("Id   Marka   Model  Year   Colour    Price    Reg_num ")
count = 0
for i in range(len(Cars)):
    if str.capitalize(Cars[i].get_car_model()) == str.capitalize(m):
        if Cars[i].get_age_car() >= n:
            Cars[i].car_print_info()
            count += 1
if count == 0:
    print("Таких автомобилей в базе нет!")






