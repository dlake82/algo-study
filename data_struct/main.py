import numpy as np
import time


class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class NodeMgmt:
    def __init__(self, value):
        self.head = Node(value)

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            return True
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return True

    def pop(self):
        node = self.head
        while node.next.next:
            node = node.next
        del node.next
        node.next = None

    def desc(self):
        if self.head == None:
            print("값이 없습니다.")
        node = self.head
        while node:
            print(node.value)
            node = node.next
        return True


class Tree:
    def __init__(self, value):
        self.head = Node(value)
        self.current_node = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            return True
        node = self.head
        parent = self.head
        while node:
            if value == node.value:
                return False
            elif value < node.value:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
        if value < parent.value:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def desc(self, head):
        if head is None:
            return
        self.desc(head.left)
        print(head.value)
        self.desc(head.right)

    def delete(self, value):
        self.head, deleted = self._delete_value(self.head, value)
        return deleted

    def _delete_value(self, node, value):
        if node is None:
            return node, False
        deleted = False
        print(node)
        if node.value == value:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif value < node.value:
            node.left, deleted = self._delete_value(node.left, value)
        else:
            node.right, deleted = self._delete_value(node.right, value)
        return node, deleted


class Heap():
    def __init__(self, value):
        self.heap_array = []
        self.heap_array.append(None)
        self.heap_array.append(value)

    def insert(self, value):
        index = len(self.heap_array) - 1
        if index == -1:
            self.heap_array.append(None)
            self.heap_array.append(value)
            return True
        self.heap_array.append(value)
        index += 1
        while index >= 1:
            parent = index // 2
            if parent == 0:
                break
            if self.heap_array[parent] > self.heap_array[index]:
                break
            else:
                self.heap_array[parent], self.heap_array[index] = self.heap_array[index], self.heap_array[parent]
                index = parent
        return True

    def pop(self):
        index = len(self.heap_array) - 1
        if index == -1:
            return False
        temp = self.heap_array[1]
        self.heap_array[1] = self.heap_array[index]
        del self.heap_array[index]
        parent = 1
        while parent < index:
                child_left = parent * 2
                child_right = parent * 2 + 1
                if child_left >= index:
                    parent = child_left
                elif child_right >= index:
                    if self.heap_array[parent] < self.heap_array[child_left]:
                        self.heap_array[parent], self.heap_array[child_left] = self.heap_array[child_left], self.heap_array[
                            parent]
                        parent = child_left
                    else: break
                else:
                    if self.heap_array[parent] < self.heap_array[child_left] or self.heap_array[parent] < self.heap_array[child_right]:
                        if self.heap_array[child_left] > self.heap_array[child_right]:
                            self.heap_array[parent], self.heap_array[child_left] = self.heap_array[child_left], self.heap_array[parent]
                            parent = child_left
                        else:
                            self.heap_array[parent], self.heap_array[child_right] = self.heap_array[child_right], \
                                                                                   self.heap_array[parent]
                            parent = child_right
                    else:break
        return temp

    def desc(self):
        for i in self.heap_array:
            print(i, end=' ') if i else 0
        print()

