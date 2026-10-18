# File Handling

with open('scores.txt', "w") as f:
    f.write("Python\nMachine Learning\nDeep Learning")

print("-----------------")

with open('scores.txt', "r") as f:
    content = f.read()
    print(content)

print("-----------------")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
with open('scores.txt', "w") as f:
    f.write(f"{name}, {age}\n")

print("-----------------")

with open('scores.txt', "r") as f:
    content = f.read()
    print(content)

print("-----------------")

# Functions and return values

def calculate_result(marks):
    total_marks = sum(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)
    average_marks = total_marks / len(marks)
    return total_marks, highest_mark, lowest_mark, average_marks
student_marks = [80, 75, 90, 65, 85]
total_marks, highest_mark, lowest_mark, average_marks = calculate_result(student_marks)
print(f"Total marks: {total_marks}")
print(f"Highest mark: {highest_mark}")
print(f"Lowest mark: {lowest_mark}")
print(f"Average marks: {average_marks}")

print("-----------------")

def calculate_bill(units):
    if units <= 100:
        rate = 10 
    elif units <= 200:
        rate = 15
    elif units <= 300:
        rate = 20
    else:
        rate = 25
    bill = units * rate
    return bill
user_units = int(input("Enter the number of units: "))
bill_amount = calculate_bill(user_units)
print(f"Bill amount for {user_units} units is {bill_amount}")

print("-----------------")

def calculate_salary(basic_salary, bonus_percentage):
    bonus = basic_salary * (bonus_percentage / 100)
    final_salary = basic_salary + bonus
    if final_salary > 100000:
        tax = final_salary * 0.1
    else:
        tax = final_salary * 0.05
    salary = final_salary - tax
    return bonus, tax, salary
user_basic_salary = float(input("Enter the basic salary: "))
bonus_percentage = float(input("Enter the bonus percentage: "))
bonus, tax, final_salary = calculate_salary(user_basic_salary, bonus_percentage)
print(f"Bonus: {bonus}")
print(f"Tax: {tax}")
print(f"Final salary: {final_salary}")


print("-----------------")

def login(username, password):
    if username == "talha" and password == "123456":
        return "Login successful!"
    elif username != "talha":
        return "Invalid username."
    else:
        return "Invalid password."

name = input("Enter your username: ")
password = input("Enter your password: ")

result = login(name, password)
print(result)

print("-----------------")

def calculate_discount(total_amount,customer_type):
    if customer_type == "regular":
        return total_amount * 0.05
    elif customer_type == "premium":
        return total_amount * 0.1
    elif customer_type == "vip":
        return total_amount * 0.20
    else:
        return 0
amount = float(input("Enter the total amount: "))
customer_type = input("Enter the customer type: ")
discount = calculate_discount(amount, customer_type)
print(f"Discount: {discount}")
final_price = amount - discount
print(f"Final price: {final_price}")
    
print("-----------------")

# Function Scope (Local and Global)

balance = 50000
def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited {amount}.")
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew {amount}.")
    else:
        print("Insufficient balance.")
def check_balance():
        return balance  
print(f"Initial Balance {balance}")
deposit(1000)
withdraw(2000)
print(f"Final Balance {balance}")

print("-----------------")

visitor_count = 0
def add_visitor():
    global visitor_count
    visitor_count += 1 
def reset_visitor():
    global visitor_count
    visitor_count = 0

add_visitor()
add_visitor()
add_visitor()
add_visitor()
add_visitor()

print(f"Total visitor count: {visitor_count}")
reset_visitor()
print(f"Total visitor count after reset: {visitor_count}")

print("-----------------")

passing_marks = 50
def check_result(marks):
    if marks < passing_marks:
        grade = "Fail"
    elif marks >= 90 and marks <= 100:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"
    return grade
marks = int(input("Enter the marks: "))
grade = check_result(marks)
print(f"Grade: {grade}")

def change_passing_marks():
    global passing_marks
    passing_marks = 40
print(f"Current Passing Marks: {passing_marks}")
print(f"Grade: {check_result(45)}")

change_passing_marks()

print(f"New Passing Marks: {passing_marks}")
print(f"Grade: {check_result(45)}")
    
print("-----------------")

game_score = 0
def add_score(points):
    global game_score
    game_score += points
    print(f"Added {points} points to the game score.")
def remove_score(points):
    global game_score
    if points <= game_score:
        game_score -= points
        print(f"Removed {points} points from the game score.")
    else:
        print("Score cannot go below 0.")
def reset_score():
    global game_score
    game_score = 0
    print("Game score reset to 0.")

add_score(50)
remove_score(20)
remove_score(50)
reset_score()

print("-----------------")

# Lambda Functions

num = int(input("Enter a number: "))

square = lambda a: a*a
print(square(num))
cube = lambda a: a*a*a
print(cube(num))

print("-----------------")

num = int(input("Enter a number: "))
n = lambda x: "Even" if x % 2 == 0 else "Odd"
print(n(num))

print("-----------------")

price = 5000
discount = 0.1
calculate_discount = lambda price, discount: price * discount
discount_amount = calculate_discount(price, discount)
print(f"Discount amount: {discount_amount}")
final_price = price - discount_amount
print(f"Final price: {final_price}")

print("-----------------")

students = [("Ali", 75), ("Talha", 90), ("Ahmed", 65), ("Usman", 85)]
sort_students = lambda students: sorted(students, key=lambda x: x[1], reverse=True)
sorted_list = sort_students(students)

for name, marks in sorted_list:
    print(f"{name}: {marks}")

print("-----------------")

# Maps and Filter

prices = [1000, 2500, 5000, 7500, 10000]
add_tax = list(map(lambda x: x * 1.15, prices))
print(add_tax)

print("-----------------")

marks = [45, 67, 78, 89, 92]
add_marks = list(map(lambda x: x + 5, marks))
print(add_marks)

print("-----------------")

marks = [35, 67, 45, 89, 50, 42, 76, 30]
get_passing_marks = list(filter(lambda x: x >= 50, marks))
print(get_passing_marks)

print("-----------------")

prices = [500, 1500, 2500, 800, 3000, 1200, 450]
get_prices = list(filter(lambda x: x >= 1000, prices))
print(get_prices)

print("-----------------")

# Inner / Nested Functions

def process_order(item, price):
    def receipt():
        print(f"Order receipt for {item} is {price}.")
    receipt()
process_order("Pizza", 2000)

print("-----------------")

def process_order(item, price):
    def receipt():
        total = price * 0.1
        final_price = price - total
        print(f"Order receipt after 10% discount for {item} is {final_price}.") 
    receipt()
process_order("Pizza", 2000)

print("-----------------")

def calculate_salary(basic_salary, bonus):
    def calculate_bonus():
        return basic_salary * bonus
    total_salary = basic_salary + calculate_bonus()
    return total_salary
print(calculate_salary(5000, 0.1))

print("-----------------")

def checkout(price, quantity):
    def  calculate_total():
        return price * quantity
    total_price = calculate_total()
    def calculate_discount():
        return total_price * 0.1
    discount_amount = calculate_discount()
    final_price = total_price - discount_amount
    return final_price
print(checkout(5000, 2))

print("-----------------")

def bank_account(balance, amount, transaction):
    def deposit(amount):
        return balance + amount
    def withdraw(amount):
        if amount <= balance:
            return balance - amount
        else:
            return "Insufficient balance"
    if transaction == "deposit":
        return deposit(amount)
    elif transaction == "withdraw":
        return withdraw(amount)
    else:
        return "Invalid transaction type"

initial_balance = 50000
action = "withdraw"
tax_amount = 5000

final_balance = bank_account(initial_balance, tax_amount, action)

print(f"Initial Balance: {initial_balance}")
print(f"Transaction: {action}")
print(f"Amount: {tax_amount}")
print(f"Final Balance: {final_balance}")
    
