
"""
Task 3: Classes
Create a class called SquareGenerator that has a method to generate squares for a given range of numbers.
"""
class SquareGenerator:

    def __init__(self):
        pass
    def squares_generator(self, start, end):
        if end < start:
            raise ValueError("End value must be grater than start value")
        squares = [i ** 2 for i in range(start, end)]
        return squares
