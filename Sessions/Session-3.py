# # ternary Expression

# age = 20
# status = "Adult" if age >= 18 else "Minor"
# print(status)

# marks = 40
# result = "Pass" if marks >= 40 else "Fail"
# print(result)

# # Break, Continue, Pass

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(6):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(20):
#     if i == 15:
#         break
#     print(i)

# for i in range(20):
#     if i % 3 == 0:
#         continue
#     print(i)

# For Loop and Enumerate


# foods = ["Pizza", "Burger", "Fish", "Chips", "Noodles"]
# for index, food in enumerate(foods):
#     print(index, food)

# for i in range(10):
#     print(i * i)

# for i in range(10):
#     square = i * 2
#     print(square)

#  While Loop

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# num = 2
# while num <= 20:
#     print(num)
#     num += 2

# num = 10
# while num >= 1:
#     print(num)
#     num -= 1

# print("Liftoff!")

# Nested Loops

for i in range(1,6):
    for j in range(1,6):
        print(i, 'x', j, '=', i*j)

for i in range(1):
    for j in range(1,6):
        print('*' * j)

# for i in range(1,6):
#     print('*' * i)

# for i in range(2,3):
#     for j in range(1,11):
#         print(i, 'x', j, '=', i*j)

