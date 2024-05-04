import math

class Circle:
    def __init__(self, radius):
        """
        Initializes a Circle object with the given radius.

        Parameters:
            radius (int or float): The radius of the circle.

        Returns:
            None
        """
        self.radius = radius

    def calculate_area(self):
        """
        Calculates the area of a circle based on the given radius.

        Returns:
            float: The calculated area of the circle.
        """
        return round(math.pi * self.radius ** 2, 2)
