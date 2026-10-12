# Session 1: 
# Variables and Data Types
# 1. Variables
# 2. Operations
# 3. Strings and String Operations
# 4. Input type Casting
# 5. Comments


name = "Talha Aleem,"
age = 21
# height = 5.8
favourite_subject = "Computer Science"

print(name, age, favourite_subject)

print(type(name))
print(type(age))
# print(type(height))
print(type(favourite_subject))

a = 10
b = 3

print(a + b)  # Addition
print(a // b)
print(a % b)  # Modulus
print(a > b)
print(a > 5 and b > 5)


a = 15
b = 4

print(a // b)
print(a % b)  # Modulus

print(a > b and b > 0)

course = "Machine Learning"

print(course.upper())
print(len(course))
print(course[0:8])
print("Learn" in course)

student, score = "Ali", 85
print(f"{student} scored {score}")

student = "Ali"
score = 85
print(student+" scored "+str(score)+" marks")

course = "Deep Learning"
print(course.lower())
print(len(course))
print("Deep" in course)
print(f"The topic is {course}.")

age = input("Enter your age: ")
age = int(age)
print(age + 5)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"{first_name} {last_name}")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(num1 * num2)

name = input("Enter your name: ")
year_of_birth = int(input("year of birth: "))
current_year = 2026
age = current_year - year_of_birth
print(f" you are {age} years old.")
