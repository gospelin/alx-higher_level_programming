#!/usr/bin/python3
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::
"""


import math


class MagicClass:

    """Class that stores the properties of a circumference

    This defines an empty square class.
    As instructed, no method or attribute is created
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """ Method that calculates the area of the circumference """
    def area(self):
        return ((self.__radius ** 2) * math.pi)

    """ Method that calculates the perimeter of a circumference """
    def circumference(self):
        return (2 * math.pi * self.__radius)
