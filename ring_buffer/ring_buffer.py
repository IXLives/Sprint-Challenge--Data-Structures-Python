from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = self.storage.head

    def append(self, item):
        # check if ring is full (tail = capacity - 1 And front == 0)
        # if full, replace tail with item
        # if not full, add to tail
        # if full, remove tail then add item to tail
        # check if full
        size = self.storage.__len__()
        if (size == self.capacity):
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if self.current == self.storage.head:
                self.current = self.current.next
            self.current = self.storage.tail

        # check if empty
        elif (self.storage.length == 0):
            self.storage.add_to_tail(item)
            size += 1
            self.current = self.storage.head

        else:
            self.storage.add_to_tail(item)
            size += 1
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        # from head of list, add items to list buffer
        # if next item is none, stop adding
        start = self.current
        if start.next is not None:
            next_node = start.next
        elif start.next is None:
            next_node = self.storage.head
        while next_node != start:
            if next_node == None:
                next_node = self.storage.head
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next
            if self.current.next == None:
                next_node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
