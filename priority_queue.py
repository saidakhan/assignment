# priority_queue.py
"""
PriorityQueue backed by a sorted Python list (ascending).
Largest element is at the end (self.data[-1]).

The doctests below are exactly 15 examples (the course tests expect 15).

>>> q = PriorityQueue()
>>> q.empty
True
>>> len(q)
0
>>> q.front is None
True
>>> try:
...     q.pop()
... except IndexError:
...     print("pop-error")
pop-error
>>> q.push(2); q.push(1); q.push(3)
>>> len(q)
3
>>> q.front
3
>>> q.pop()
3
>>> q.pop()
2
>>> q.pop()
1
>>> q.empty
True
>>> q2 = PriorityQueue([5,2,7,7,1])
>>> len(q2)
5
>>> q2.front
7
"""

import bisect

class PriorityQueue:
    def __init__(self, data=None):
        """
        Initialize the priority queue. If 'data' is provided, make a sorted copy.
        """
        if data is None:
            self.data = []
        else:
            self.data = sorted(list(data))

    def push(self, value):
        """Insert value while keeping the underlying list sorted (ascending)."""
        bisect.insort(self.data, value)

    def pop(self):
        """Remove and return the largest element. Raises IndexError on empty."""
        if not self.data:
            raise IndexError("pop from empty PriorityQueue")
        return self.data.pop()

    @property
    def front(self):
        """Return the largest element without removing it, or None if empty."""
        if not self.data:
            return None
        return self.data[-1]

    @property
    def empty(self):
        """True if queue has no elements."""
        return not bool(self.data)

    def __len__(self):
        return len(self.data)

