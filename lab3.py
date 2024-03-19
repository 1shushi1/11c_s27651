import math
from  square_generator.square_generator import SquareGenerator

"""
Task1:
List Comprehensions Write a Python program that generates a list of squares of numbers from 1 to 10 using list comprehension.ares
"""

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
# squares = SquareGenerator()
# print(squares.squares_generator(1, 11))
"""
Task 4: Libraries
Utilize the math library to calculate the square root of each number in the generated list from the previous task.
"""
# squares = SquareGenerator()
# print([math.sqrt(i) for i in squares.squares_generator(1, 11)])

"""
Task 5: Exceptions
Handle the case where the end of the range is less than the start in the SquareGenerator class.
"""
# squares = SquareGenerator()
# print([math.sqrt(i) for i in squares.squares_generator(10, 9)])

"""
Task 6: Modules
Extract the SquareGenerator class into a separate module named square_generator.py.
"""
# squares = SquareGenerator()
# print(squares.squares_generator(1, 11))

"""
Task 7: Packages
Transform the square_generator module into a package by adding an empty __init__.py file and organize it accordingly.
"""


