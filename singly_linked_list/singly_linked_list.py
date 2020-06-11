"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

"""Our singly-linked list class. It holds references to
the list's head and tail nodes."""
class SinglyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            dummy = ListNode(value, self.head)
            self.head = dummy

        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.length == 0:
            return None

        value = self.head.value

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        self.head = self.head.next

        self.length -= 1
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length == 0:
            return None
            
        value = self.tail.value
        
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        pointer = self.head
        while pointer.next != self.tail:
            pointer = pointer.next

        self.tail = pointer
        self.tail.next = None

        self.length -= 1
        return value

    """Returns True if node with given value exists in
    the list. Returns False otherwise."""
    def contains(self, value):
        if self.length == 0:
            return None

        pointer = self.head
        while pointer != None and pointer.value != value:
            pointer = pointer.next

        if pointer == None:
            return False
        return True

    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.length == 0:
            return None

        max_value = None
        pointer = self.head
        while pointer != None:
            if max_value == None or pointer.value > max_value:
                max_value = pointer.value
            pointer = pointer.next
        
        return max_value