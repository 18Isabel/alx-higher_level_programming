#!/usr/bin/python3
"""
Rectangle class module.

Define Rectangle class.
"""


class Rectangle:
    """Define a rectangle.
    width (int)(default=0): the width of the rectangle.
    height (int)(default=0): the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Define width property."""
        return self.__width

    @property
    def height(self):
        """Define height property."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        value (int): the new length of the width.
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        value (int): the new length of the height.
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Return the area of the rectangle."""
        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
