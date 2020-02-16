import sys
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.length = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        return DoublyLinkedList.add_to_head(self, value)

    def dequeue(self):
        return DoublyLinkedList.remove_from_tail(self)

    def len(self):
        return self.length
