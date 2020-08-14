from names.queue import Queue
from names.stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
                return
            return self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
                return
            return self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)

        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

    def get_max(self):
        if self.right is None:
            return self.value

        return self.right.get_max() 

    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)   

    def in_order_print(self, node):
        if node is not None:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)


    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)



    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)