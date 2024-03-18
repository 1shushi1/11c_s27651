"""
Task1:
List Comprehensions Write a Python program that generates a list of squares of numbers from 1 to 10 using list comprehension.ares
"""
def squares():
    squares = [i ** 2 for i in range(1, 11)]
    print(squares)
squares()