import math


"""
Task1:
List Comprehensions Write a Python program that generates a list of squares of numbers from 1 to 10 using list comprehension.ares
"""
from SquareGenerator import SquareGenerator

# def squares():
#     squares = [i ** 2 for i in range(1, 11)]
#     print(squares)
# squares()

"""
Task 2: Functions
Expand the previous program by defining a function that takes a range of numbers as input and returns a list of squares for that range.e_squares(start, end))
"""

# def e_squares(start, end):
#     squares = [i ** 2 for i in range(start, end)]
#     return squares
# print(e_squares(1, 11))

"""
Task 3: Classes
Create a class called SquareGenerator that has a method to generate squares for a given range of numbers.
"""
# square_generator = SquareGenerator()
# print(square_generator.squares_generator(1, 11))

"""
Task 4: Libraries
Utilize the math library to calculate the square root of each number in the generated list from the previous task.
"""
square_generator = SquareGenerator()
print([math.sqrt(i) for i in square_generator.squares_generator(1, 11)])





