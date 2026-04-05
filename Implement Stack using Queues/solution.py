class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self._head = None 
        self._tail = None

    def push(self, x):
        node = Node(x)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node

    def pop(self):
        val = self._head.val
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        return val

    def peek(self):
        return self._head.val

    def size(self):
        count = 0
        cur = self._head
        while cur:
            count += 1
            cur = cur.next
        return count

    def is_empty(self):
        return self._head is None


class MyStack(object):

    def __init__(self):
        self._q1 = Queue() 
        self._q2 = Queue()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._q2.push(x)
        while not self._q1.is_empty():
            self._q2.push(self._q1.pop())
        self._q1, self._q2 = self._q2, self._q1
        

    def pop(self):
        """
        :rtype: int
        """
        return self._q1.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self._q1.peek()
        

    def empty(self):
        """
        :rtype: bool
        """
        return self._q1.is_empty()
        

