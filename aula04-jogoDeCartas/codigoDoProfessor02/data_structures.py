from typing import List, Optional, Any


class Stack:
    def __init__(self):
        self._data: List[Any] = []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        try:
            if not self._data:
                raise IndexError("Pop from empty stack")
            return self._data.pop()
        except IndexError as e:
            print(e)
        return None

    def peek(self) -> Any:
        try:
            if not self._data:
                raise IndexError("Peek from empty stack")
            return self._data[-1]
        except IndexError as e:
            print(e)
        return None

    def is_empty(self) -> bool:
        return len(self._data) == 0


class Queue:
    def __init__(self):
        self._data: List[Any] = []

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        try:
            if not self._data:
                raise IndexError("Dequeue from empty queue")
            return self._data.pop(0)
        except IndexError as e:
            print(e)
        return None

    def peek(self) -> Any:
        try:
            if not self._data:
                raise IndexError("Peek from empty queue")
            return self._data[-1]
        except IndexError as e:
            print(e)
        return None

    def is_empty(self) -> bool:
        return len(self._data) == 0


class CircularQueue:
    def __init__(self, capacity: int):
        self._data: List[Optional[Any]] = [None] * capacity
        self._head = 0
        self._tail = 0
        self._count = 0
        self._capacity = capacity

    def enqueue(self, item: Any) -> None:
        try:
            if self._count == self._capacity:
                raise OverflowError("CircularQueue is full")
            self._data[self._tail] = item
            self._tail = (self._tail + 1) % self._capacity
            self._count += 1
        except OverflowError as e:
            print(e)

    def dequeue(self) -> Any:
        try:
            if self._count == 0:
                raise IndexError("Dequeue from empty CircularQueue")
            item = self._data[self._head]
            self._data[self._head] = None
            self._head = (self._head + 1) % self._capacity
            self._count -= 1
            return item
        except OverflowError as e:
            print(e)
        return None

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return self._count == self._capacity


class ElementPriority:

    def __init__(self, data, priority):
        self._data: List[Any] = data
        self._priority = priority

    def get_priority(self):
        return self._priority

    def get_data(self):
        return self._data

    def set_priority(self, new_priority):
        self._priority = new_priority

    def set_data(self, new_data):
        self._data = new_data


class PriorityQueue:
    def __init__(self):
        self._data: List[ElementPriority] = []

    def enqueue(self, element, priority):
        element_priority = ElementPriority(element, priority)
        index_to_insert = self._get_priority_index(element_priority)
        self._data = self._data[:index_to_insert] + [element_priority] + self._data[index_to_insert:]

    def _get_priority_index(self, element: ElementPriority):
        index_to_insert = 0
        for data in self._data:
            if element.get_priority() > data.get_priority():
                return index_to_insert
            index_to_insert += 1
        return index_to_insert

    def dequeue(self) -> Any:
        try:
            if not self._data:
                raise IndexError("Pop from empty PriorityQueue")
            element_priority = self._data.pop(0)
            return element_priority.get_data()
        except IndexError as e:
            print(e)
        return None

    def peek(self) -> Any:
        try:
            if not self._data:
                raise IndexError("Peek from empty PriorityQueue")
            element_priority = self._data[0]
            return element_priority.get_data()
        except IndexError as e:
            print(e)
        return None

    def is_empty(self) -> bool:
        return len(self._data) == 0

    @staticmethod
    def is_full() -> bool:
        return False


class BinarySearchTree:
    class Node:
        def __init__(self, value: Any):
            self.value = value
            self.left: Optional[BinarySearchTree.Node] = None
            self.right: Optional[BinarySearchTree.Node] = None

    def __init__(self):
        self.root: Optional[BinarySearchTree.Node] = None

    def insert(self, value: Any) -> None:
        if not self.root:
            self.root = self.Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node: Node, value: Any) -> None:
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = self.Node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = self.Node(value)

    def inorder(self) -> List[Any]:
        result: List[Any] = []

        def traverse(node: Optional[BinarySearchTree.Node]):
            if node:
                traverse(node.left)
                result.append(node.value)
                traverse(node.right)

        traverse(self.root)
        return result


class BinaryHeap:
    def __init__(self):
        self._data: List[Any] = []

    def push(self, item: Any) -> None:
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> Any:
        try:
            if not self._data:
                raise IndexError("Pop from empty heap")
            root = self._data[0]
            last = self._data.pop()
            if self._data:
                self._data[0] = last
                self._sift_down(0)
            return root
        except IndexError as e:
            print(e)
        return None

    def peek(self) -> Any:
        try:
            if not self._data:
                raise IndexError("Peek from empty heap")
            return self._data[0]
        except IndexError as e:
            print(e)
        return None

    def _sift_up(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            if self._data[idx] < self._data[parent]:
                self._data[idx], self._data[parent] = self._data[parent], self._data[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx: int) -> None:
        n = len(self._data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right

            if smallest == idx:
                break

            self._data[idx], self._data[smallest] = self._data[smallest], self._data[idx]
            idx = smallest



