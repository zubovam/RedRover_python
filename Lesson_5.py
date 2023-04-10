# OOP

# class Dog:
#     biology_class = 'Animal'
#     def __init__(self, name, weight, color):
#         self.__name = name
#         self.weight = weight
#         self.color = color
#
#     def run(self):
#         return 'I can run!'
#
#     def get_name(self):
#         return f'Hello! My name is {self.__name}'
#
#     def set_name(self, new_name):
#         self.__name = new_name


# class Pitbull(Dog):
#
#     def __init__(self, name, weight, color, passport):
#         super().__init__(name, weight, color)
#         self.passport = passport
#
#     def give_a_pow(self):
#         return 'I can give a paw'
#
#     def run(self):
#         return 'I can run fast!'


# dog1 = Dog('Bobik', 3, 'brown')
# print(dog1.name)
# print(dog1.get_name())
# print(dog1.color)
# print(dog1.biology_class)
#
# dog2 = Dog('Rex', 7, 'black')
# print(dog2.biology_class)
# print(dog2.get_name())
#
# dog3 = Pitbull('Lassie', 8, 'black', 'type1')

# print(dog3.get_name())
# print(dog3.biology_class)
# print(dog3.give_a_pow())
# print(dog3.passport)
# print(dog2.run())
# print(dog3.run())
# print(dog2.__dict__)
# print(dog2.get_name())
# print(dog2.set_name('Snoopy'))/
# print(dog2.get_name())
# print(dog2.__dict__)
# print(dog2._Dog__name)


# OOP Review Review Review Review Review Review Review Review Review Review Review Review


# class Car:
#     name = "Q7"
#     make = "audi"
#     age = 2020
#
#     def start(self):
#         print('Заводим двигатель', args)
#
#     def stop(self):
#         print('Выключаем двигатель')
#
#
# car1 = Car()
# car2 = Car()
# print(type(car1))
# print(car1.age)
# print(car1.name)
# print(car1.make)
# car1.start()
# Car.start()
# print(car1.start())

# class Car:
#     name = "Priora"
#     make = "Lada"
#     age = 2020
#
#     def start(self, name, make='Audi'):
#         self.name = name
#         self.make = make
#         print(f'У машины {self.make} {self.name} заведен двигатель')
#
#     def get_age(self):
#         print(f'Машина {self.make} {self.name} {self.age} выпуска')
#
#
# car3 = Car()
# print(car3.make)
# print(car3.start('Q7'))
# print(car3.get_age())

# class Cat:
#
#     name = 'Timmy'
#
#     def __init__(self):
#         print('Hello')
#
#
# Cat()

# class HockeyPlayer:
#     def __init__(self, first_name, last_name, goal=0, asist=0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.goal = goal
#         self.asist = asist
#
#     def goals(self, goal=0):
#         self.goal = goal
#
#     def all_asist(self, asist=0):
#         self.asist = asist
#
#     def statistics(self):
#         print(f'Hockey pleyer: {self.first_name} {self.last_name} \nGoals:{self.goal}\nAsist: {self.asist}')
#
#
# ovi = HockeyPlayer('Alexendr', 'Ovechkin')
# ovi.goals(700)
# ovi.all_asist(500)
# ovi.statistics()
#
# vin = HockeyPlayer('Vinsent', 'Lekavele')
# vin.goals(500)
# vin.all_asist(600)
# vin.statistics()

# class Person:  # Parent
#     def can_breath(self):
#         print('Я дышу')
#
#     def can_walk(self):
#         print('Я хожу')
#
#     def can_sleep(self):
#         print('Я сплю')
#
#
# class Teacher(Person):  # Subclass
#     def can_teach(self):
#         print('Учитель учит')
#
#     def can_breath(self):
#         print('Учитель дышит')
#
#
# t1 = Teacher()
# t1.can_walk()
# t1.can_sleep()
# t1.can_teach()
# t1.can_breath()
# p = Person()
# p.can_breath()

# print(issubclass(Teacher, Person))
# print(issubclass(Person, object))
# print(issubclass(Teacher, object))

# class Animals:
#     def can_breath(self):
#         print('Могу дыштаь')
#
#
# class Dogs:
#     def can_bark(self):
#         print('Wow-wow')
#
#
# class Beagle(Animals, Dogs):
#     def can_sleep(self):
#         print('Бигль спит')


# b1 = Beagle()
# b1.can_breath()
# b1.can_bark()
# b1.can_sleep()
# print(Beagle.__mro__)

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info(self):
#         print(f'Кошка {self.name} возраста {self.age}')
#
#     def speak(self, sound):
#         self.sound =sound
#         print(f'Кошка сказала {self.sound}')
#
#
# c1 = Cat('Дынька', 7)
# c1.get_info()
# c1.speak('Мяу')
