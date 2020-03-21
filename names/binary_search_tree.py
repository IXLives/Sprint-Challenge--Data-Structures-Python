from dll_stack import Stack
from dll_queue import Queue

import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None  # BinarySearchTree
        self.right = None  # BinarySearchTree

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to current node
        # if smaller go left
        # if greater go right
        # if no node to go to (left or right)
        # make new node at that spot
        if self.value <= value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        if self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):

        # compare value to current node value
        # if smaller, go left
        # if larger, go right
        # if equal return true
        # if smaller but no left
        # return false
        # if larger but no right
        # return false

        if self.value < target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        if self.value == target:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        # maximum value should be the rightmost value on the tree
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        if self.left:
            self.left.for_each(cb)

        cb(self.value)

        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # use a queue
        # add current node to q
        # while q is not empty
        # add current node's children to q
        # pop current node
        node_queue = Queue()
        curNode = node
        node_queue.enqueue(curNode)
        while node_queue.len() > 0:
            traverse = node_queue.dequeue()
            if traverse.left:
                node_queue.enqueue(traverse.left)
            if traverse.right:
                node_queue.enqueue(traverse.right)
            print(traverse.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a node stack
        # push the current node onto stack
        # while we have items on stack
        # push left value of current node if we can
        # print current value and pop it off
        # push the right value of current node if we can
        # init stack
        node_stack = Stack()
        curNode = node

        while True:
            # this reaches the left most node of the current node
            if curNode is not None:
                # add node to stack as pointer before traversing to left
                node_stack.push(curNode)
                # set current node to its left child until its left child is none
                curNode = curNode.left
            # if stack is not empty
            elif node_stack.len() > 0:
                # pop current node before we check its right children
                curNode = node_stack.pop()
                # print
                print(curNode.value)
                # go right until there is no more right
                curNode = curNode.right
            else:
                # if curnode is none and no other conditions are true we are done
                break
        # first pass below
        # while node_stack.len() > 0:
        #     if curNode.left:
        #         leftNode = curNode.left
        #         node_stack.push(leftNode.value)
        #         curNode = leftNode
        #     print(node_stack.pop())
        #     if curNode.right:
        #         rightNode = curNode.right
        #         node_stack.push(rightNode.value)
        #         curNode = rightNode

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)
