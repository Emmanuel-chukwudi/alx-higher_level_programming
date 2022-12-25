#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize a new class"""
        self.size = size

    @property
    def size(self):
        """"
        Getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Area of square
        """
        return (self.__size)**2

    def my_print(self):
        """Print the square with the # character."""
        for rows in range(0, self.__size):
            [print("#", end="") for i in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")


if __name__ == "__main__":
    Square()
