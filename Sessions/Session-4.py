# # Functions and Return Values

# def add_numbers(a, b):
#     result = a + b
#     return result
# total = add_numbers(5, 3)
# print(total)

# def square(n):
#     return n * n
# print(square(5))
# print(square(10))
# print(square(15))

# def greet(name):
#     greeting = f"Hello, {name}!"
#     return greeting
# print(greet("Talha"))

# def square(n):
#     return n * n
# user_n = int(input("Enter a number: "))
# print(square(user_n))

# def greet(name):
#     greeting = f"Hello, {name}!"
#     return greeting
# user_name = input("Enter your name: ")
# print(greet(user_name))

# Function Scope (Local and Global)

# x = 10
# def my_func():
#     y = 5
#     print(x + y)
# my_func()
# # print(y)

# a = 20
# def my_func2():
#     b = 30
#     print(a)
#     print(b)
# my_func2()

# def my_func3():
#     c = 40
# my_func3()
# print(c)

# Lambda Functions

# square = lambda x: x * x
# print(square(5))

# add = lambda a, b: a + b
# print(add(3, 4))

# mutiply = lambda a, b: a * b
# print(mutiply(3, 4))

# num = lambda x: x % 2 == 0
# print(num(4))
# print(num(5))

# x = int(input("Enter a number: "))
# num = lambda x: x % 2 == 0
# print(num(x))

# Map and Filter

# nums = [1, 2, 3, 4, 5]

# squared = list(map(lambda x: x * x, nums))
# print(squared)

# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)

# temp = [27, 28, 29, 30, 31]
# temperature = list(map(lambda x: x * 1.8 + 32, temp))
# print(temperature)

# num =[3, 4, 7, 10, 11, 13, 14, 16]
# greater = list(filter(lambda x: x > 10, num))
# print(greater)

# Nested Functions
# def outer(text):
#     def inner():
#         print("Inner function says:", text)
#     inner()
# outer("Hello")

# def process_order(item):
#     def receipt():
#         print(f"Order receipt for {item} is 2000.")
#     receipt()
# process_order("Pizza")

# b
# def process_order(item, price):
#     price=price*0.1
#     def receipt():
#         print(f"Order receipt for {item} is {price}.")
#     receipt()
# process_order("Pizza", 2000)

# File handling

# with open('notes.txt', "w") as f:
#     f.write("Hello Talha")

with open('notes.txt', "r") as f:
    content = f.read()
    print(content)
