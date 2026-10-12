# #  lists

# cities = ["Lahore", "Karachi", "Islamabad", "Peshawar", "Quetta"]

# cities.append("Multan")
# cities.remove("Quetta")

# print(cities[1])
# print(cities[-1])
# print(len(cities))


# # tuple
# colors = (34, 159, 230)
# print(colors[0])
# print(colors[1])
# print(colors[2])

# print(len(colors))

# # dictionary

# student = { "name": "Ali", "age": 20}
# print(student["name"])
# student["age"] = 21
# student["city"] = "Lahore"
# for key, value in student.items():
#     print(key, ':', value)


# book = {"title": "Python Programming", "author": "John Doe", "year": 2021}
# for key, value in book.items():
#     # print(key, ':', value)
#     print(key)
# for key, value in book.items():
#     print(value)

# book["year"] = 2026
# print(book["year"])

# sets

nums = {1 ,2, 2, 3, 3, 3}
print(nums)
nums.add(4)
print(nums)
nums.remove(1)
print(nums)
print(3 in nums)

# nums = {2, 1, 1, 4, 4, 4, 3, 3}
# set = set(nums)
# print(set)

# list = [2, 1, 1, 4, 4, 4, 3, 3]
# print(list)

#  conditaional statement

# marks = 75
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 70:
#     print("Grade: B")
# else:
#     print("fail")

# marks = 65
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 70:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# elif marks >= 40:
#     print("Grade: D")
# else:
#     print("fail")

# age = 20
# has_ticket = True
# if age >= 18:
#     if has_ticket:
#         print("You are allow for the entry of the Event")
#     else:
#         print("You are not allow for the entry of the Event")
# else:
#     print("You are not allow for the entry of the Event")

# age = int(input("Enter your age: "))
# has_ticket = bool(input("Do you have a ticket?"))

# if age >= 18:
#     if has_ticket:
#         print("You are allowed for the event")
#     else:
#         print("You are not allowed for the event")
# else:
#     print("Your age must be equal or greater than 18 to attend the event")

