# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 23                   | #
# | 12866 돌 그룹             | #
# ---------------------------- #


def run():
    A, B, C = sorted(map(int, r_input().split()))
    
    visit = set()
    visit.add((A, B, C))
    queue = deque([(A, B, C)])

    while queue:
        a, b, c = queue.popleft()

        if a == b == c:
            print(1)
            sys.exit()

        if a != b:
            X, Y = 2 * a, b - a
            A, B, C = sorted([X, Y, c])

            if (A, B, C) not in visit:
                queue.append((A, B, C))
                visit.add((A, B, C))
            
        if b != c:
            X, Y = 2 * b, c - b
            A, B, C = sorted([X, Y, a])

            if (A, B, C) not in visit:
                queue.append((A, B, C))
                visit.add((A, B, C))

        if a != c:
            X, Y = 2 * a, c - a
            A, B, C = sorted([X, Y, b])

            if (A, B, C) not in visit:
                queue.append((A, B, C))
                visit.add((A, B, C))
    
    print(0)


if __name__ == "__main__":
    run()
