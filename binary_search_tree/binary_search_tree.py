import sys
sys.path.append('../queue')
from myqueue import Queue
sys.path.append('../stack')
from stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        if target > self.value and self.right != None:
            return self.right.contains(target)
        elif target < self.value and self.left != None:
            return self.left.contains(target)

        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left != None:
            self.left.for_each(fn)

        fn(self.value)
        
        if self.right != None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left != None:
            self.left.in_order_print(self.left)

        print(node.value)

        if self.right != None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)

        while len(queue) != 0:
            current = queue.dequeue()
            print(current.value)

            if current.left != None:
                queue.enqueue(current.left)
            if current.right != None:
                queue.enqueue(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)

        while len(stack) != 0:
            current = stack.pop()
            print(current.value)

            if current.left != None:
                stack.push(current.left)
            if current.right != None:
                stack.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
