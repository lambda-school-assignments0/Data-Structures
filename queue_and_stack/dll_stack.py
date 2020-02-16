import sys
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.length = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        return DoublyLinkedList.add_to_head(self, value)

    def pop(self):
        return DoublyLinkedList.remove_from_head(self)

    def len(self):
        return self.length
