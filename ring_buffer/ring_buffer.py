from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if ring is full (tail = capacity - 1 And front == 0)
        # if full, replace tail with item
        # if not full, add to tail
        # if full, remove tail then add item to tail
        # check if full
        size = self.storage.__len__()
        oldest = 0
        if (size == self.capacity):
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
        # check if empty
        elif (self.storage.length == 0):
            self.storage.add_to_tail(item)
            size += 1
        else:
            self.storage.add_to_tail(item)
            size += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        # from head of list, add items to list buffer
        # if next item is none, stop adding
        self.current = self.storage.head
        while self.current != None:
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
