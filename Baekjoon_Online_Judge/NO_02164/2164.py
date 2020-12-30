# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 30                             | #
# | 2164 카드 2                        | #
# -------------------------------------- #


def run():
    N = int(r_input())

    deq = deque(list(range(1, N + 1)))

    for _ in range(N - 1):
        deq.popleft()
        deq.rotate(-1)
    
    print(deq[0])


if __name__ == "__main__":
    run()
