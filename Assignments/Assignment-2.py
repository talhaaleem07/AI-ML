# List

# You have the following marks:
# marks = [75, 82, 90, 65, 88]
# Perform these tasks:
# Add a new mark 95.
# Remove the mark 65.
# Find the highest mark.
# Find the lowest mark.
# Calculate the average marks.
# Sort the marks in ascending order.
# Print the final list.

marks = [75, 82, 90, 65, 88]
marks.append(95)
marks.remove(65)
print(marks)
print(max(marks))
print(min(marks))
print(sum(marks) / len(marks))
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

# tuples

# Create a tuple containing:
# Employee ID
# Name
# Department
# Salary
# Experience Years

# Perform these tasks:
# Print the employee name.
# Print the department.
# Print the salary.
# Find the total number of values in the tuple.
# Check whether "Talha" exists in the tuple.
# Try changing the salary.

employee_info = (101, "Talha", "IT", 50000, 5)
print(employee_info[1])
print(employee_info[2])
print(employee_info[3])
print(len(employee_info))
print("Talha" in employee_info)

# Dictionary

# Create a dictionary:
# Perform these tasks:
# Print the student's name.
# Add a new key called "university".
# Update the CGPA.
# Add "skills" with at least 3 programming skills.
# Remove the "age" key.
# Print all keys.
# Print all values.
# Print the complete dictionary.

student_profile = {
    "name": "Talha",
    "age": 21,
    "CGPA": 3.5,
    "skills": ["Python", "Java", "C++"],
}
print(student_profile["name"])
student_profile["university"] = "GCU"
student_profile["CGPA"] = 3.8
student_profile["skills"].append("JavaScript")
del student_profile["age"]

for key, value in student_profile.items():
    print(key)
for key, value in student_profile.items():
    print(value)

print(student_profile)

# set

# You have two developers:
# Perform these tasks:
# Find the skills both developers have.
# Find all unique skills.
# Find skills only Developer 1 has.
# Find skills only Developer 2 has.
# Add "Docker" to Developer 1.
# Remove "Java" from Developer 2.
# Print the updated sets.

developer_1 = {"Python", "JavaScript", "React", "Node.js"}
developer_2 = {"Python", "Java", "React", "MongoDB"}

print(developer_1.intersection(developer_2))
print(developer_1.union(developer_2))
print(developer_1.difference(developer_2))
print(developer_2.difference(developer_1))
developer_1.add("Docker")
developer_2.remove("Java")
print(developer_1)
print(developer_2)


# If / Elif / Else

# Problem 1: Student Grade System
# Ask the user to enter their percentage.
# Rules:
# 90–100 → A+
# 80–89  → A
# 70–79  → B
# 60–69  → C
# 50–59  → D
# Below 50 → Fail
# Below 0 or above 100 → Invalid Percentage

marks = int(input("Enter your Percentage:"))

if marks >= 90 and marks <= 100:
    print("A+")
elif marks >= 80 and marks < 90:
    print("A")
elif marks >= 70 and marks < 80:
    print("B")
elif marks >= 60 and marks < 70:
    print("C")
elif marks >= 50 and marks < 60:
    print("D")
else:
    print("Fail")


# Problem 2: ATM Withdrawal
# Rules:
# Withdrawal must be greater than 0.
# Withdrawal cannot be greater than the balance.
# Withdrawal amount must be divisible by 500.
# If valid, calculate the remaining balance.

Account_Balance = int(input("Enter your Account Balance:"))
Withdrawal_Amount = int(input("Enter your Withdrawal Amount:"))
if Withdrawal_Amount > 0 and Withdrawal_Amount <= Account_Balance and Withdrawal_Amount % 500 == 0:
    remaining_balance = Account_Balance - Withdrawal_Amount
    print(f"Your remaining balance is {remaining_balance}")
else:
    print("Invalid withdrawal amount.")

# Problem 3: Job Eligibility Checker
# Rules:
# The candidate is eligible if:
# Age is at least 18
# Experience is at least 1 year
# Education is "BS Computer Science"
# Give meaningful messages explaining why the candidate is not eligible.

Age = int(input("Enter your Age:"))
Experience = int(input("Enter your Experience:"))
Education = input("Enter your Education:")
if Age >= 18 and Experience >= 1 and Education == "BS Computer Science":
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")

# Problem 4: Electricity Bill Calculator
# Ask the user to enter electricity units consumed.
# Calculate the bill:
# 0–100 units       → Rs. 10 per unit
# 101–200 units     → Rs. 15 per unit
# 201–300 units     → Rs. 20 per unit
# Above 300 units   → Rs. 25 per unit

units = float(input("Enter the number of units consumed:"))
if units <= 100:
    rate = 10
elif units <= 200:
    rate = 15
elif units <= 300:
    rate = 20
else:
    rate = 25
bill = units * rate
print(f"Your bill is {bill}")

# Problem 5: Movie Ticket Booking ⭐
# Ask the user:
# Name
# Age
# Number of Tickets
# Ticket Type
# Ticket types:
# Regular → Rs. 1000
# Premium → Rs. 2000
# VIP → Rs. 3500
# Age discounts:
# Below 12 → 50% discount
# 60 or above → 30% discount
# Others → No discount
# Calculate:
# Ticket Price
# Total Price
# Discount
# Final Price

name = input("Enter your name:")
age = int(input("Enter your age:"))
num_tickets = int(input("Enter the number of tickets:"))
ticket_type = input("Enter the ticket type (Regular, Premium, VIP):").lower()

if ticket_type == "regular":
    rate = 1000
elif ticket_type == "premium":
    rate = 2000
elif ticket_type == "vip":
    rate = 3500
else:
    print("Invalid ticket type.")
    rate = 0

ticket_price = rate
total_price = num_tickets * ticket_price

if age < 12:
    discount = total_price * 0.5
elif age >= 60:
    discount = total_price * 0.3
else:
    discount = 0

discount = total_price - discount
final_price = total_price - discount

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Number of tickets: {num_tickets}")
print(f"Ticket type: {ticket_type}")
print(f"Ticket price: {ticket_price}")
print(f"Total price: {total_price}")
print(f"Discount: {discount}")
print(f"Final price: {final_price}")
