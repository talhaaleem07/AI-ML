# # Exception Handling

# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ZeroDivisionError:
#     print('Cannot divide by zero!')
# except ValueError:
#     print('That is not a valid number')
# finally:
#     print('Done trying.')

# try:
#     num_1=int(input("Enter a Number:"))
#     num_2=int(input("Enter a Number:"))
#     print(num_1 / num_2)
# except ZeroDivisionError:
#     print('Cannot divide by zero!')
# except ValueError:
#     print('This is not a valid number')
# finally:
#     print('Done trying.')

# oops

# Classes, Objects and Inheritence

# Classes and Objects

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"Hi, I am {self.name}")

# s1 = Student('Ali', 20)
# s1.greet()        

# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#     def description(self):
#         print(f"This Car's Brand is {self.brand} and its manufacturing year is {self.year}.")

# s1 = Car('Toyota', 2019)
# s1.description()

# # 2 is missing

# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#     # def description(self):
#     #     print(f"This Car's Brand is {self.brand} and its manufacturing year is {self.year}.")

# s1 = Car('Toyota', 2019)
# s2 = Car('Honda', 2020)

# print(s1.brand)
# print(s2.year)

# # Instance vs Class Variable and Methods

# class student:
#     school = 'NAVTTC'
#     def __init__(self, name):
#         self.name = name

# s1 = student('Ali')
# s2 = student('Sara')
# print(s1.school, s2.school)
# print(s1.name)

# class Employee:
#     company = 'NAVTTC'
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
# s1 = Employee('Ali', 'Software Engineer')
# print(s1.name, s1.position)
# print(s1.company)

# class Employee:
    
#     def __init__(self, name, position, company):
#         self.name = name         
#         self.position = position 
#         self.company = company

# e1 = Employee('Ali', 'Software Engineer', 'NAVTTC')
# e2 = Employee('Sara', 'Data Scientist', 'NETSOL')
# e3 = Employee('John', 'Product Manager', 'NAVTTC')

# # 2. Print their individual details
# print(f"Employee 1: {e1.name} ({e1.position})")
# print(f"Employee 2: {e2.name} ({e2.position})")
# print(f"Employee 3: {e3.name} ({e3.position})")

# print("\n--- Company Value Confirmation ---")
# if e1.company == e2.company == e3.company:
#     print(f"Confirmed! All employees share the same company: '{Employee.company}'")
# else:
#     print("Verification failed.")

# Constructors and Destructors

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print(f'{self.name} created')

#     def __del__(self):
#         print(f'{self.name} destroyed')

# s1 = Student('Ali')
# del s1

# class Book:
#     def __init__(self, title):
#         self.title = title
#         print(f"Book {self.title} has been added.")

#     def __del__(self):
#         print(f"Book {self.title} has been removed.")

# s1 = Book('Python for Beginners')
# del s1

# class Animal:
#     def eat(self):
#         print('Eating')
# class Dog(Animal):
#     def bark(self):
#         print('Barking')
# d = Dog()
# d.eat()
# d.bark()

# class vehicle:
#     def start(self):
#         print('Vehicle started')
# class car(vehicle):
#     def honk(self):
#         print('Honking the car')
# c = car()
# c.start()
# c.honk()


class Shape:
    def display(self):
        print("This is a shape")
class Circle(Shape):
    def draw_circle(self):
        print("Drawing Circle")
class Square(Shape):
    def draw_square(self):
        print("Drawing Square")

circle = Circle()
square = Square()

circle.display()
circle.draw_circle()

square.display()
square.draw_square()

# Assignment
# Access modifier, private, public, protected name managing page 10 Day 3 