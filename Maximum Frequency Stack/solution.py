class Node:
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self._top = None

    def push(self, x):
        node = Node(x)
        node.next = self._top
        self._top = node

    def pop(self):
        val = self._top.key
        self._top = self._top.next
        return val

    def peek(self):
        return self._top.key

    def is_empty(self):
        return self._top is None


class LinkedList:
    def __init__(self):
        self._head = None

    def get(self, key, default=None):
        cur = self._head
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return default

    def set(self, key, val):
        cur = self._head
        while cur:
            if cur.key == key:
                cur.val = val
                return
            cur = cur.next
        node = Node(key, val)
        node.next = self._head
        self._head = node


class FreqStack(object):

    def __init__(self):
        self._freq = LinkedList()   
        self._group = LinkedList()   
        self._max_freq = 0
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        freq = self._freq.get(val, 0) + 1
        self._freq.set(val, freq)

        if freq > self._max_freq:
            self._max_freq = freq

        stack = self._group.get(freq)
        if stack is None:
            stack = Stack()
            self._group.set(freq, stack)
        stack.push(val)

        

    def pop(self):
        """
        :rtype: int
        """
        stack = self._group.get(self._max_freq)
        val = stack.pop()

        if stack.is_empty():
            self._max_freq -= 1

        self._freq.set(val, self._freq.get(val) - 1)

        return val
        

