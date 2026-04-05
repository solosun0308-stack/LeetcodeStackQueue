class Node:
    def __init__(self, val):
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
        val = self._top.val
        self._top = self._top.next
        return val

    def peek(self):
        return self._top.val

    def is_empty(self):
        return self._top is None

class MyQueue(object):

    def __init__(self):
        self._s1 = Stack()  
        self._s2 = Stack() 
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while not self._s1.is_empty():
            self._s2.push(self._s1.pop())
        self._s1.push(x)
        while not self._s2.is_empty():
            self._s1.push(self._s2.pop())
        

    def pop(self):
        """
        :rtype: int
        """
        return self._s1.pop()

        

    def peek(self):
        """
        :rtype: int
        """
        return self._s1.peek()

        

    def empty(self):
        """
        :rtype: bool
        """
        return self._s1.is_empty()

        
