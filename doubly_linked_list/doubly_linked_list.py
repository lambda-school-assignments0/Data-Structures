"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
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
        if self.length > 0:
            self.head.prev = ListNode(value, None, self.head)
            self.head = self.head.prev
        elif self.length == 0:
            self.head = ListNode(value, None, None)
            self.tail = self.head
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        removed_node_value = self.head.value
        self.head = self.head.next
        if self.length == 1:
            self.tail = self.tail.next
        self.length -= 1
        return removed_node_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.length == 0:
            self.head = ListNode(value, None, None)
            self.tail = self.head
            self.length += 1
        else:
            current = self.head
            while current != None and current.next != None:
                current = current.next
            current.next = ListNode(value, current, None)
            self.tail = current.next
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        current = self.head
        while current.value != None and current.next != None:
            current = self.head.next
        removed_node_value = self.tail.value
        self.tail = current.prev
        self.length -= 1
        if self.length == 0:
            self.head = None
        current = None
        return removed_node_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # delete the node from List
        self.delete(node)
        # insert node to head
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # delete the node from List
        self.delete(node)
        # insert node to tail
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # handle edge case - if only one element in List
        if self.length == 1 and self.head.value == node.value:
            self.head = None
            self.tail = None

        # handle edge case - if node is head
        elif self.head.value == node.value:
            self.head = self.head.next
            self.head.prev = None

        # handle edge case - if node is tail
        elif self.tail.value == node.value:
            self.tail = self.tail.prev
            self.tail.next = None

        # handle all other cases
        else:
            # find the node
            current = self.head
            while current.value != node.value:
                current = current.next
            # remove the node
            current.prev.next, current.next.prev = current.next, current.prev

        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        current = self.head
        maximum_node_value = current.value
        while current.next != None:
            current = current.next
            if current.value > maximum_node_value:
                maximum_node_value = current.value
        return maximum_node_value
