#!/usr/bin/python3
"""Class linked list try"""


class Node:
    """class content"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (isinstance(value, int)):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is None or isinstance(value, Node)):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """class SinglyLinkedList"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        item = Node(value)
        if self.__head is None:
            item.next_node = None
            self.__head = item
        elif self.__head and self.__head.data > value:
            item.next_node = self.__head
            self.__head = item
        else:
            tmp = self.__head
            while (tmp and tmp.next_node and tmp.next_node.data < value):
                tmp = tmp.next_node
            item.next_node = tmp.next_node
            tmp.next_node = item

    def __str__(self):
        printable = []
        lst = self.__head
        while lst is not None:
            printable.append(str(lst.data))
            lst = lst.next_node
        return ('\n'.join(printable))
