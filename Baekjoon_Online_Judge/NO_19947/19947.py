# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 06                             | #
# | 19947 투자의 귀재 배주형            | #
# -------------------------------------- #


if __name__ == "__main__":
    H, Y = map(int, r_input().split())

    maximum = H

    queue = deque([(H, Y)])

    while queue:
        money, rem_year = queue.popleft()

        maximum = max(maximum, money)

        if rem_year >= 1:
            queue.append((int(money * 1.05), rem_year - 1))
        
        if rem_year >= 3:
            queue.append((int(money * 1.2), rem_year - 3))
        
        if rem_year >= 5:
            queue.append((int(money * 1.35), rem_year - 5))

    print(maximum)
