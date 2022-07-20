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


class Node:
    """ A class that defines a square by its size

    This defines an empty square class.
    As instructed, no method or attribute is created
    """
    def __init__(self, data, next_node=None):
        """ Method that returns the position value
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Method that returns the position value
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Method that returns the position value
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Method that returns the position value
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Method that returns the position value
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ A class that defines a square by its size

    This defines an empty square class.
    As instructed, no method or attribute is created
    """
    def __str__(self):
        """ Method that returns the position value
        """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """ Method that returns the position value
        """
        self.__head = None

    def sorted_insert(self, value):
        """ Method that returns the position value
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
