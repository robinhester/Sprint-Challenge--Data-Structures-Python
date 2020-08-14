class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

        def insert_after(self, value):
            current_next = self.next
            self.next = ListNode(value, self, current_next)
            if current_next:
                current_next.prev = self.next

        def insert_before(self, value):
            current_prev = self.prev
            self.prev = ListNode(value, current_prev, self)
            if current_prev:
                current_prev.next = self.prev

        def delete(self):
            if self.prev:
                self.prev.next = self.next
            if self.next:
                self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        else:
            self.tail = new_node
            self.head = new_node

    def remove_from_tail(self):
        value = self.tail.value

        if not self.tail:
            return

        elif self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1

        return value

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def delete(self, node):
        self.length -= 1

        if not self.head and not self.tail:
            print('Try Again Young Jedi')
            return 

        elif self.head == self.tail:
            self.head = None
            self.tail = None

        elif node == self.head:
            self.head = node.next
            self.head.prev = None

        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        
        else:
            node.delete()

    def get_max(self):
        highest_value = self.head.value
        current_node = self.head

        while current_node is not None:
            if current_node.value > highest_value:
                highest_value = current_node.value

            current_node = current_node.next

        return highest_value