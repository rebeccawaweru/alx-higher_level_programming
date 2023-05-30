#!/usr/bin/python3

"""Defines a node of a singly linked list"""


class Node:
    """Representing a node in the list"""

    def __init__(self, data, next_node=None):
        """A new node
        Args:
        data: integer data of the new node
        next_node: the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Acquire data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Acquire the next node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Representing a singly-linked list"""

    def __init__(self):
        """A new singlylinked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new node
        Args:
        value: the new Node
        """
        y = Node(value)
        if self.__head is None:
            y.next_node = None
            self.__head = y
        elif self.__head.data > value:
            y.next_node = self.__head
            self.__head = y
        else:
            x = self.__head
            while (x.next_node is not None and x.next_node.data < value):
                x = x.next_node
            y.next_node = x.next_node
            x.next_node = y

    def __str__(self):
        """Defining the print()"""
        arry = []
        x = self.__head
        while x is not None:
            arry.append(str(x.data))
            x = x.next_node
        return ('\n'.join(arry))
