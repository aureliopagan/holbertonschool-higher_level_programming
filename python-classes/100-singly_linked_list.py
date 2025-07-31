"""Module for implementing a singly linked list."""

class Node:
    """Node class for a singly linked list."""
    
    def __init__(self, data, next_node=None):
        """Initialize a Node with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the Node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node of the Node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class."""
    
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node with the given value in sorted order."""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the singly linked list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
