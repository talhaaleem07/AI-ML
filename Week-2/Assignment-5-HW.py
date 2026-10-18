# Multiple inheritance & Method Resolution Order (MRO)

class Flyer:
    def move(self):
        print('Flying')
class Swimmer:
    def move(self):
        print('Swimming')
class Duck(Swimmer, Flyer):
    pass
Duck().move()

class Camera:
    def capture(self):
        print('Capturing the Pic')
class Phone:
    def call(self):
        print('Calling the Person')
class SmartPhone(Camera, Phone):
    pass
SmartPhone().capture()
SmartPhone().call()
# b
print(SmartPhone.__mro__)

# Access Specifiers & Name Mangling

class Account:
    def __init__(self, balance):
        self.balance = balance
        self._pin = 123456
        self.__password = 'secret'
a = Account(1000)
print(a.balance)
print(a._pin)
print(a._Account__password)
# print(a.__password)

class BankAccount:
    def __init__(self, account_holder, branch, pin):
        self.account_holder = account_holder
        self._branch = branch
        self.__pin = pin
b = BankAccount('Alice', 'Main Branch', 123456)
print(b.account_holder)
print(b._branch)
print(b._BankAccount__pin)
# print(b.__pin)

# Inner Classes, Association, Aggregation, Composition

# Inner Class

class Library:
    class Book:
        def __init__(self, title):
            self.title = title
        def display(self):
            print(self.title)
book = Library.Book('Python for Beginners')
book.display()

# Association

class Teacher:
    def __init__(self, name):
        self.name = name
class Student:
    def __init__(self, name):
        self.name = name
    def learn(self, teacher):
        print(f"{self.name} is learning from {teacher.name}")

teacher = Teacher('Mr. Smith')
student = Student('Alice')
student.learn(teacher)

# Aggregation

class Teacher:
    def __init__(self, name):
        self.name = name
class Department:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
    def display(self):
        print("Department:", self.name)
        print("Teacher:", self.teacher.name)
teacher1 = Teacher("Ali")
department1 = Department("Math", teacher1)
department1.display()

# Composition

class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()
        print("Car is driving")
car1 = Car()
car1.drive()

class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine = Engine()
    def start_car(self):
        self.engine.start()
        print("Car started")
car1 = Car()
car1.start_car()

# Polymorphism & Advanced OOP Concepts

# Polymorphism and Operator Overloading

class Cat:
    def speak(self):
        print("Meow")
class Dog:
    def speak(self):
        print("Woof")
for animal in [Cat(), Dog()]:
    animal.speak()

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
sq = Square(4)
circle = Circle(5)

shapes = [sq, circle]
for shape in shapes:
    print("Area:", shape.area())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y      
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)
    def display(self):
        print(f"Point: ({self.x}, {self.y})")
p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
p3.display()

# Magic / Dunder Functions

class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return self.title
b = Book("Python for Beginners")
print(b)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.price}" 
p = Product("Python for Beginners", 29.99)
print(p)

class ShopingCart:
    def __init__(self, item):
        self.item = item
    def __len__(self):
        return len(self.item)
cart = ShopingCart(["Laptop","Mouse","Keyboard","Monitor"])
print(len(cart))

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


student1 = Student("Talha", 22)
student2 = Student("Talha", 22)

print(student1 == student2)

# Dynamic Polymorphism (Subclass as Base Class)

#  overriding

class Employee:
    def pay (self):
        print("Employee receives basic salary")
class Manager(Employee):
    def pay (self):
        print("Manager receives higher salary") 
emp = Employee()     
emp.pay()
mgr = Manager() 
mgr.pay()

# Dynamic Polymorphism

class Employee:
    def pay (self):
        print("Employee receives basic salary")
class Manager(Employee):
    def pay (self):
        print("Manager receives higher salary") 

emp = [Employee(), Manager()]
for employee in emp:
    employee.pay()

class Shape:
    def area(self):
        print('Area not defined')

class Circle(Shape):
    def area(self):
        print('Area of circle is 3.14 * radius^2')
shapes = [Shape(), Circle()]
for shape in shapes:
    shape.area()

class Employee:
    def pay (self):
        print("Employee receives basic salary")
class Manager(Employee):
    def pay (self):
        print("Manager receives higher salary") 
emp = [Employee(), Manager()]
for employee in emp:
    employee.pay()

# Abstract Methods & Classes, Data Classes, keyword Arguments

# Abstract Class

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
Rectangle = Rectangle(4, 5)
print(Rectangle.area())

# Data Class

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

student = Student("Talha", 22)
print(student)

# keyword Arguments

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
student = Student(
    name="Talha",
    age=22
)
print(student)

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
p = Point(x = 3, y = 5)
print(p)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rec = Rectangle(4, 5)
print(rec.area())

from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
student = Student(name="Talha", age=22)
print(student)