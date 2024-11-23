#Big O Notation

# Enqueue: O(1)
# Dequeue: O(1)
# Peek: O(1)
# Is Empty: O(1)

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0
