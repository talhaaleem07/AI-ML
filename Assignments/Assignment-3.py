# Looping Techniques

# Enumerate

words = ['hello', 'world', 'python', 'programming']

for index, word in enumerate(words):
    print(index, word)

# ----------------------------------------------

print()

# zip

a = [1, 2, 3]
b = [4, 5, 6]

for x, y in zip(a, b):
    print(x, y)

# ----------------------------------------------

print()

#  items

p1 = {'name': 'Ali', 'age': 20, 'city': 'New York'}

for key, value in p1.items():
    print(key, value)

# ----------------------------------------------

print()

# sorted

num = [1, 5, 3, 6, 7, 8, 9, 4, 2]

print("Sorted list:")
for n in sorted(num):
    print(n, end=" ")

print("\nSorted list without duplicates:")
for n in sorted(set(num)):
    print(n, end=" ")

# ----------------------------------------------

print()

# reversed

num = [1, 5, 3, 6, 7, 8, 9, 4, 2]

print("Reversed list:")
for n in reversed(num):
    print(n, end=" ")

# ----------------------------------------------

print()

# While Loop with If Condition

count = 0

while count < 5:
    if count == 3:
        print("Count is 3")
    count += 1

# ----------------------------------------------

print()

# Continue

for i in range(1, 11):
    if i == 6:
        continue
    print(i, end=" ")

# ----------------------------------------------

print()

# Break

a = [1, 3, 5, 7, 9, 11]
val = 7

for i in a:
    if i == val:
        print(f"Found at {i}!")
        break
else:
    print(f"not found")

# ----------------------------------------------

print()

# For Loop

a = ["Geeks", "for", "Geeks"]
for i in a:
    print(i)

# ----------------------------------------------
print()

s = "Geeks"
for i in s:
    print(i)

# ----------------------------------------------
print()

for i in range(0, 10, 2):
    print(i)

# ----------------------------------------------
print()

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# ----------------------------------------------
print()

b = ["eat", "sleep", "repeat"]
for i, j in enumerate(b):
    print (i, j)

# ----------------------------------------------

print()

# While Loop

count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")

# ----------------------------------------------
print()

i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1

# ----------------------------------------------
print()

a = 'geeksforgeeks'
i = 0
while i < len(a):
    i += 1
    pass
  
print('Value of i :', i)

# ----------------------------------------------
print()

i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
    print(a[i])
    i += 1

# ----------------------------------------------
print()

i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No Break")

# ----------------------------------------------

# print()

# Nested Loops

for i in range(1, 6):
    for j in range(1, 11):
        print(i,'x',j,'=',i*j)

# ----------------------------------------------
print()

num = int(input("Enter a number: "))
for i in range(1, num+1):
    for j in range(1, num+1):
        print(i, end=" ")
    print()

# ----------------------------------------------
print()

students = ["Ali", "Talha", "Ahmad",]
subjects = ["Python", "JavaScript", "Java"]

for student in students:
    for subject in subjects:
        print(f"{student} is learning {subject}")
        
# ----------------------------------------------
print()

num = int(input("Enter a number: "))
for i in range(1):
    for j in range(1, num+1):
        print('*' * j)

# ----------------------------------------------
print()

rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# ----------------------------------------------
print()

rows = int(input("Enter rows: "))

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# ----------------------------------------------
print()

matrix_1 = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix_2 = [
    [7, 8, 9],
    [10, 11, 12]
]
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[i])):
        result = matrix_1[i][j] + matrix_2[i][j]
        print(result, end=" ")
    print()