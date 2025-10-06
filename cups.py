#!/usr/bin/env python3
# cups.py
"""
fill_cups(cups) — return minimum seconds to fill all cups.

Rules:
- each second you can fill two cups of DIFFERENT types, or one cup.
- cups is an iterable of three nonnegative ints.

Greedy: always pick two largest nonzero types and decrement them.
"""

import sys
from priority_queue import PriorityQueue

def fill_cups(cups):
    """
    >>> fill_cups([1,4,2])
    4
    >>> fill_cups([5,4,4])
    7
    >>> fill_cups([0,0,0])
    0
    >>> fill_cups([0,1,0])
    1
    """
    pq = PriorityQueue([c for c in cups if c > 0])
    seconds = 0
    # take two largest each second while possible
    while len(pq) > 1:
        a = pq.pop()
        b = pq.pop()
        a -= 1
        b -= 1
        seconds += 1
        if a > 0:
            pq.push(a)
        if b > 0:
            pq.push(b)
    # if one type left, you need that many more seconds (one per second)
    if len(pq) == 1:
        seconds += pq.pop()
    return seconds

def main(argv=None, stdin=None):
    if argv is None:
        argv = sys.argv[1:]
    if stdin is None:
        stdin = sys.stdin
    for line in stdin:
        parts = line.strip().split()
        if not parts:
            continue
        nums = list(map(int, parts))
        # homework expects three ints per case; we slice to first 3
        print(fill_cups(nums[:3]))

if __name__ == "__main__":
    main()
