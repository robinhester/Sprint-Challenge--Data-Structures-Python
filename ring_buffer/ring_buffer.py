from ring_buffer.doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, value):
        if self.current is None:
            self.current = self.storage.head
            
        if self.storage.length == self.capacity:
            self.current.value = value
            self.current = self.current.next

        else:
            self.storage.add_to_tail(value)



    def get(self):
        array = []

        current = self.storage.head

        while current:
            array.append(current.value)

            current = current.next

        return array

    