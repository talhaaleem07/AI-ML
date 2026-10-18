# 2 practice problems of each topic

print("Variables")
print()
# 1. Variables

# 1. Employee Salary Record
# Create variables for an employee:
# name, department, basic_salary, bonus, tax, experience_years
# Then create variables to calculate/store:

name = "Ali"
department = "Data Science"
basic_salary = 50000
bonus = 10000
tax = 3000
experience_years = 5

total_salary = basic_salary + bonus - tax
print(f"Employee {name} from {department} department has a basic salary of {basic_salary} bonus of {bonus}, tax of {tax} and total salary of {total_salary} after tax.")

# ----------------------------------------------

print()

# 2. Product Information
# Create variables for a product:
# product_name, price, quantity, category, in_stock
# and calculate the total value of all available laptops.

product_name = "Laptop"
price = 100000
quantity = 11
category = "Electronics"
in_stock = True

total_value = price * quantity
print(f"Total value of {quantity} {product_name} is {total_value}.")

# ----------------------------------------------

print() 

print("Operations")
print()
# 2. Operations

# 1. Shopping Bill
# Perform the following:
# Calculate the total price.
# Calculate a 10% discount.
# Calculate the final price after discount.
# Calculate the amount paid if the customer gives you 150000.
# Calculate the remaining change.

laptop = 110000
mouse = 5000
keyboard = 10000

total_price = laptop + mouse + keyboard
discount = total_price * 0.1  
final_price = total_price - discount  
amount_paid = 150000
change = amount_paid - final_price 

print(f"Total price: {total_price}")
print(f"Discount: {discount}")
print(f"Final price: {final_price}")
print(f"Amount paid: {amount_paid}")
print(f"Change: {change}")

# ----------------------------------------------

print()

# A student has marks in 5 subjects:
# Calculate:
# Total marks, Obtained marks, Percentage, Average marks
# Assume each subject has a maximum of 100.

english = 90
math = 85
physics = 90
computer = 95
stats = 80

total_marks = 100 * 5
obtained_marks = english + math + physics + computer + stats
percentage = (obtained_marks / total_marks) * 100
average_marks = obtained_marks / 5

print(f"Total marks: {total_marks}")
print(f"Obtained marks: {obtained_marks}")
print(f"Percentage: {percentage}%")
print(f"Average marks: {average_marks}")

# ----------------------------------------------

print()

print("Strings and String Operations")
print()
# 3. Strings and String Operations

# 1.Sentence Analyzer
# Create this string:
# sentence = "Python is an amazing programming language"
# Perform the following operations:
# Print the sentence in uppercase.
# Print the sentence in lowercase.
# Print the number of characters.
# Print the first character.
# Print the last character.
# Replace "amazing" with "powerful".
# Check whether "Python" exists in the sentence.
# Print the sentence in reverse.

sentence = "Python is an amazing programming language"
print(sentence.upper())
print(sentence.lower())
print(len(sentence))
print(sentence[0])
print(sentence[-1])
print(sentence.replace("amazing", "powerful"))
print("Python" in sentence)
print(sentence[::-1])


# ----------------------------------------------

print()

# 2.Username Generator
# Create a username that looks like:
# first.last
# Your program should:
# Convert both names to lowercase.
# Combine them with a . between them.
# Store the result in a variable called username.
# Print the username.

first_name = "Ali"
last_name = "Khan"
username = first_name.lower() + "." + last_name.lower()
print(f"Username: {username}")

# ----------------------------------------------

print()

print("Input type Casting")
print()
# 4. Input type Casting

# 1. Add Two Numbers
# Ask the user for two numbers:
# Convert them to integers and calculate:
# Addition
# Subtraction
# Multiplication
# Division

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")    
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")

# ----------------------------------------------

print()

# 2. Shopping Calculator
# Ask the user:
# Enter product name:
# Enter price:
# Enter quantity:
# Calculate:
# total-price

product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total_price = price * quantity

print(f"Total price for {quantity} {product_name} is: {total_price}")


# ----------------------------------------------