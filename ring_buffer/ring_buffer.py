from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = self.storage.head
        self.size = self.storage.__len__()

    def append(self, item):
        # check if ring is full (tail = capacity - 1 And front == 0)
        # if full, replace tail with item
        # if not full, add to tail
        # if full, remove tail then add item to tail
        # check if full

        if (self.size == self.capacity):
            removed = self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if self.current is None or self.current.next is None:
                self.current = self.storage.head
            if removed == self.current:
                self.current = self.storage.tail

        # check if empty
        elif (self.storage.length == 0):
            self.storage.add_to_tail(item)
            self.size += 1
            if self.current is None or self.current.next is None:
                self.current = self.storage.head

        else:
            self.storage.add_to_tail(item)
            self.size += 1
            if self.current is None or self.current.next is None:
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        # from head of list, add items to list buffer
        # if next item is none, stop adding
        start = self.current
        if start is None:
            list_buffer_contents.append(None)
        else:
            list_buffer_contents.append(start.value)

        while len(list_buffer_contents) < self.size and start is not None:
            if start is not None and start.next is not None:
                start = start.next
                list_buffer_contents.append(start.value)
            else:
                start = self.storage.head
                list_buffer_contents.append(start.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
