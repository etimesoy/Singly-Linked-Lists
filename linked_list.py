from __future__ import annotations
from typing import List


def check_type(func):
    def wrapper(self, value, *args, **kwargs):
        result = func(self, value, *args, **kwargs)
        if self.value_type is None:
            self.value_type = type(value)
        if self.value_type == type(value):
            return result
        else:
            raise TypeError
    return wrapper


class Node:
    def __init__(self, value=None, next_nd: Node = None):
        self.value = value
        self.next_nd = next_nd

    def __str__(self):
        return str(self.value)


class LinkedListIterator:
    def __init__(self, current_element):
        self.current_element = current_element

    def __next__(self):
        if self.current_element is None:
            raise StopIteration
        tmp = self.current_element
        self.current_element = self.current_element.next_nd
        return tmp

    def __iter__(self):
        return self


class SinglyLinkedList:
    def __init__(self, lst: List = None):
        self.length = 0
        self.head = self.last = None
        self.value_type = None
        if lst is not None:
            self.value_type = type(lst[0])
            for elem in lst:
                self.add_to_end(elem)

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __len__(self):
        return self.length

    @check_type
    def add_to_end(self, elem):
        self.length += 1
        if self.head is None:
            self.last = self.head = Node(elem)
        else:
            self.last.next_nd = self.last = Node(elem)

    @check_type
    def add_to_begin(self, x):
        self.length += 1
        if self.head is None:
            self.last = self.head = Node(x)
        else:
            self.head = Node(x, self.head)

    def __getitem__(self, index):
        if index > self.length - 1:
            raise ValueError

        node_now = self.head
        for i in range(index):
            node_now = node_now.next_nd

        return node_now.value

    def is_empty(self):
        return self.head is None

    def delete(self, i):
        if self.head is None:
            return

        if i == 0:
            self.head = self.head.next_nd
            return

        old = current = self.head
        count = 0
        while current is not None:
            if count == i:
                if current.next_nd is None:
                    self.last = current
                else:
                    old.next_nd = current.next_nd
                break
            old = current
            current = current.next_nd
            count += 1

    @check_type
    def insert(self, x, index):
        if self.head is None:
            self.last = self.head = Node(x, None)
            return
        if index == 0:
            self.head = Node(x, self.head)
            return
        current = self.head
        count = 0
        while current is not None:
            count += 1
            if count == index:
                current.next_nd = Node(x, current.next_nd)
                if current.next_nd.next_nd is None:
                    self.last = current.next_nd
                break
            current = current.next_nd

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = str(current.value)
            while current.next_nd is not None:
                current = current.next_nd
                out += ' ' + str(current.value)
            return out
        return ''


if __name__ == '__main__':
    empty_linked_lst = SinglyLinkedList()
    print('empty_linked_lst:', empty_linked_lst)
    empty_linked_lst.add_to_end(1);
    print('empty_linked_lst:', empty_linked_lst)
    linked_lst = SinglyLinkedList([1, 2, 3])
    print('linked_lst:', linked_lst)
    print('length of linked_lst:', len(linked_lst))
    for i in range(len(linked_lst)):
        print('linked_lst[', i, '] = ', linked_lst[i], sep='', end=', ')
    print()
    for element in linked_lst:
        print(f'iteration element: {element}')
    linked_lst.add_to_begin(0)
    print('linked_lst after adding 0 to begin:', linked_lst)
    linked_lst.insert(5, 1)
    print('linked_lst after inserting 5 on 1st position:', linked_lst)
    linked_lst.delete(3)
    print('linked_lst after deleting 3:', linked_lst)
    print('linked_lst is empty:', linked_lst.is_empty())
