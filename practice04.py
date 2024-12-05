# 1 задание


#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_len(self):
#         return round(2 * (3.14 * self.radius))
#
#     def get_circle_area(self):
#         return 3.14 * (self.radius) ** 2
#
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def get_side(self):
#         return self.side * 4
#
#     def get_square_area(self):
#         return self.side*self.side
#
#
# class SquareInCircle(Circle, Square):
#     def __init__(self, radius, side):
#         super().__init__(radius,side)
#
#
#     def get_circle_area(self):
#         return 3.14 * (self.radius) ** 2
#

# ball = Circle(40)
# print(ball.get_len())
# print(ball.get_circle_area())
#
# tetr = Square(10)
# print(tetr.get_square_area())
# print(tetr.get_side())
#
# tetr_in_ball = SquareInCircle(40, 10)
# print(tetr_in_ball.get_side())
# print(tetr_in_ball.get_square_area())
#
# # 2 задание
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

# wh = Wheels("winter","78")
# eng = Engine("4","carbon")
# drs = Doors("4","oak")
# bmv = Automobile(wh,eng,drs)
# bmv.get_info_auto()


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


class HomePet:
    def __init__(self, name, type_a, sound):
        self.__name = name
        self.__type_a = type_a
        self.__sound = sound

    @property
    def name(self):
        return self.__name

    @property
    def sound(self):  # Provide the simple sound
        return self.__sound

    @property
    def type(self):
        return f"это животное типа {self.__type_a}"

    def say_sound(self):
        return f"{self.__name} издает звуки"


class Dog(HomePet):
    def __init__(self, name,type_a,sound):
        super().__init__(name,type_a,sound)

    def say_sound(self):
        print(f"{self.name} Лает {self.sound}")


#
class Cat(HomePet):
    def __init__(self, name, type_a, sound):
        super().__init__(name, type_a, sound)

    def say_sound(self):
        print(f" {self.name} мяукает {self.sound}")

class Hamster(HomePet):
    def __init__(self, name,type_a,sound):
        super().__init__(name, type_a, sound)

    def say_sound(self):
        print(f" {self.__name} пищит {self.__sound}")


class Parrot(HomePet):
    def __init__(self, name,type_a,sound):
        super().__init__(name, type_a, sound)

    def say_sound(self):
        return f"{self.name} разговаривает и издает звук {self.sound}"


        print(f"{self.__name} разговаривает и издает звук {self.__sound}")

# my_hamster = Dog("Kesha", "Rodent", "пищит")
# print(my_hamster.get_sound())


kesha = Cat("kesha",'bird',"кар")
print(kesha.say_sound())
# kesha.get_type()
# kesha.get_name()

# kesha.get_type()
# kesha.get_name()


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
