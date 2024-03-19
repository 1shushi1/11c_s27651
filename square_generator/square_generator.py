"""
Task 3: Classes
Create a class called SquareGenerator that has a method to generate squares for a given range of numbers.
"""

"""
Task 6: Modules
Extract the SquareGenerator class into a separate module named square_generator.py.
"""


class SquareGenerator:
    def squares_generator(self, start, end):
        if end < start:
            raise ValueError("End value must be grater than start value")
        squares = [i ** 2 for i in range(start, end)]
        return squares


"""
Task 8: Inheritance
Create a subclass called CubicGenerator that inherits from the SquareGenerator class. Modify the CubicGenerator to generate cubes instead of squares.
"""

# class CubicGenerator(SquareGenerator):
#     def cubes_generator(self, start, end):
#         cubes = [i ** 3 for i in range(start, end)]
#         return cubes

"""
Task 9: Function Overriding
Override the square generation method in the Cubic Generator class to generate squares with a check to see if the start of the range is less than the end, 
if not return an Exceptions
"""


class CubicGenerator(SquareGenerator):
    def squares_generator(self, start, end):
        if start < end:
            squares = [i ** 2 for i in range(start, end)]
        else:
            raise ValueError("End value must be grater than start value")
        return squares