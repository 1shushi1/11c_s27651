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

def e_squares(start, end):
    squares = [i ** 2 for i in range(start, end)]
    return squares
print(e_squares(1, 11))