# 1 задание



class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_len(self):
        return round(2 * (3.14 * self.radius))

    def get_circle_area(self):
        return round(3.14 * (self.radius ** 2))


class Square:
    def __init__(self, side):
        self.side = side

    def get_perimetr(self):
        return self.side * 4

    def get_square_area(self):
        return self.side*self.side


class SquareInCircle(Circle, Square):
    def __init__(self, radius, side):
        Circle.__init__(self, radius)
        Square.__init__(self, side)

# через супер нельзя парамтры передавать при множественом наследовании вернее можно но не больше одного
# видимо супер работает только на первый класс при множественом наследовании дальше он не понимает
# просто заметка для себя
    def get_circle_area(self):
        return 3.14 * (self.radius) ** 2

# я незнаю насколько верно получилось с точки зрения математики я не очень силен
# я все формулы из интернета взял в последнем классе переопределил функцию так как
# по формуле это нахождения площади квадрата через радиус круга и мне показалось что это подоходит под задание
# возможно надо было в финальном классе все вычисления делать находить периметр квадрата строну через радиус или диаметр
# в задании этого не указано сделал как понял


ball = Circle(40)
print(ball.get_len())
print(ball.get_circle_area())

tetr = Square(10)
print(tetr.get_square_area())
print(tetr.get_perimetr())

tetr_in_ball = SquareInCircle(40, 10)
print(tetr_in_ball.get_perimetr())
print(tetr_in_ball.get_square_area())


# 2 задание
# class Wheels:
#     def __init__(self, type_rubber, load_index):
#         self.__type_rubber = type_rubber
#         self.__load_index = load_index

#     @property
#     def type_rubber(self):
#         return self.__type_rubber
#
#     @property
#     def load_index(self):
#         return self.__load_index
#
#     @type_rubber.setter
#     def type_rubber(self, new_type):
#         self.type_rubber = new_type
#
#
# class Engine:
#     def __init__(self, count_cilindres, material):
#         self.__count_cilindres = count_cilindres
#         self.__material = material
#
#     @property
#     def count_cilindres(self):
#         return self.__count_cilindres
#
#     @property
#     def material(self):
#         return self.__material
#
#     @count_cilindres.setter
#     def count_cilindres(self, new_amount):
#         self.__count_cilindres = new_amount
#
#
# class Doors:
#     def __init__(self, count_doors, material_doors):
#         self.__count_doors = count_doors
#         self.__material_doors = material_doors
#
#     @property
#     def count_doors(self):
#         return self.__count_doors
#
#     @property
#     def material_doors(self):
#         return self.__material_doors
#
#     @count_doors.setter
#     def count_doors(self, new_amount):
#         self.__type_rubber = new_amount
#
#
# class Automobile:
#     def __init__(self, obj_wheels, obj_engine, obj_doors):
#         self.obj_wheels = obj_wheels
#         self.obj_engine = obj_engine
#         self.obj_doors = obj_doors
#
#     def display_info_auto(self):
#         print(self.obj_wheels.type_rubber,"тип резины")
#         print(self.obj_wheels.load_index,"индекс загрузки")
#
#         print(self.obj_engine.material,"материал двигателя")
#         print(self.obj_engine.count_cilindres,"количество цилиндров")
#
#         print(self.obj_doors.count_doors,"количество дверей")
#         print(self.obj_doors.material_doors,"материал двери")
#
#
#
# wh = Wheels("winter","78")
# eng = Engine("4","carbon")
# drs = Doors("4","oak")
# bmv = Automobile(wh,eng,drs)
# bmv.display_info_auto()
#

# class Wheels:
#     def __init__(self, type_rubber, load_index):
#         self.__type_rubber = type_rubber
#         self.__load_index = load_index
#
#     @property
#     def type_rubber(self):
#         return self.__type_rubber
#
#     @property
#     def load_index(self):
#         return self.__load_index
#
#     @type_rubber.setter
#     def type_rubber(self, new_type):
#         self.type_rubber = new_type
#
#
# class Engine:
#     def __init__(self, count_cilindres, material):
#         self.__count_cilindres = count_cilindres
#         self.__material = material
#
#     @property
#     def count_cilindres(self):
#         return self.__count_cilindres
#
#     @property
#     def material(self):
#         return self.__material
#
#     @count_cilindres.setter
#     def count_cilindres(self, new_amount):
#         self.__count_cilindres = new_amount
#
#
# class Doors:
#     def __init__(self, count_doors, material_doors):
#         self.__count_doors = count_doors
#         self.__material_doors = material_doors
#
#     @property
#     def count_doors(self):
#         return self.__count_doors
#
#     @property
#     def material_doors(self):
#         return self.__material_doors
#
#     @count_doors.setter
#     def count_doors(self, new_amount):
#         self.__type_rubber = new_amount
#
#
# class Automobile:
#     def __init__(self, obj_wheels, obj_engine, obj_doors):
#         self.obj_wheels = obj_wheels
#         self.obj_engine = obj_engine
#         self.obj_doors = obj_doors
#
#     def get_info_auto(self):
#         print(self.obj_wheels.type_rubber)
#         print(self.obj_wheels.load_index)
#
#         print(self.obj_engine.material)
#         print(self.obj_engine.count_cilindres)
#
#         print(self.obj_doors.count_doors)
#         print(self.obj_doors.material_doors)
#

# здесь я столкнулся с некоторой сложностью  я так понял когда мы защищаем параметры
# мы не можем их использовать в других классах которые наследуются и поэтому надо писать геттеры
# либо я что то не так сделал
# я хотел изначально через 3 функции сделать
# когда в задании указывается защитить поля
# написание _name с одним подчеркивание считается за защиту?
# просто если нет я бы тогда  написал через проперти  у меня в прошлом комите через него написано
# я надеюсь вы мне не снизите за это бал
# class HomePet:
#     def __init__(self, name, type_a, sound):
#         self._name = name
#         self._type_a = type_a
#         self._sound = sound
#
#     def get_name(self):
#         return f"Его зовут {self._name}"
#
#     def get_type(self):
#         return f"Это животное типа {self._type_a}"
#
#     def get_sound(self):
#         return f"{self._name} издает звук {self._sound}."
#
# class Dog(HomePet):
#     def __init__(self, name, type_a, sound):
#         super().__init__(name, type_a, sound)
#
#     def get_sound(self):
#        return f"{self._name} Лает {self._sound}"
#
#
# #
# class Cat(HomePet):
#     def __init__(self, name, type_a, sound):
#         super().__init__(name, type_a, sound)
#
#     def get_sound(self):
#         return f" {self._name} мяукает {self._sound}"
#
#
# class Hamster(HomePet):
#     def __init__(self, name, type_a, sound):
#         super().__init__(name, type_a, sound)
#
#     def get_sound(self):
#         return f" {self._name} пищит {self._sound}"
#
#
# class Parrot(HomePet):
#     def __init__(self, name, type_a, sound):
#         super().__init__(name, type_a, sound)
#
#     def get_sound(self):
#         return f"{self._name} разговаривает {self._sound}"
#
# # my_hamster = Dog("Kesha", "Rodent", "пищит")
# # print(my_hamster.get_sound())
#
#
# kesha = Cat("kesha", 'bird', "кар")
# print(kesha.get_sound())
# print(kesha.get_name())
# print(kesha.get_type())
#



# class Employer:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#
#     def print_info(self):
#         print("This is employer class", "his name", self.name, self.last_name, "his age", self.age)
#
#     def __int__(self):
#         print("magic")
#         return int(self.age)
#
#     def __str__(self):
#         return f"{self.name} разобрался с работой методов стр и инт"
#
#
# class President(Employer):
#     def __init__(self, name, last_name, age):
#         super().__init__(name, last_name, age)
#
#     def print_info(self):
#         print("This is President class", "his name", self.name, self.last_name, "his age", self.age)
#
#
# class Manager(Employer):
#     def __init__(self, name, last_name, age):
#         super().__init__(name, last_name, age)
#
#     def print_info(self):
#         print("This is Manager class", "his name", self.name, self.last_name, "his age", self.age)
#
#
# class Worker(Employer):
#     def __init__(self, name, last_name, age):
#         super().__init__(name, last_name, age)
#
#     def print_info(self):
#         print("This is Worker class", "his name", self.name, self.last_name, "his age", self.age)
#
#
# emp = Employer("андрей", "никанов", "24")
#
# man = Manager("Дмитрий", "Нормальнов", "27")
#
# emp.print_info()
# man.print_info()
