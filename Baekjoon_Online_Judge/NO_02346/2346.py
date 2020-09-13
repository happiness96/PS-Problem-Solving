# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 13                             | #
# | 2346 풍선 터뜨리기                  | #
# -------------------------------------- #


def run():
    N = int(r_input())
    ballons = list(map(int, r_input().split()))
    queue = deque(range(1, N + 1))

    for _ in range(N):
        print(queue[0], end=' ')
        rem_ballons = len(queue)

        mv = ballons[queue.popleft() - 1]

        if mv > 0:
            mv -= 1
        
        if rem_ballons != 1:
            mv %= (rem_ballons - 1)

        while mv and queue:
            if mv > 0:
                queue.append(queue.popleft())
                mv -= 1

            else:
                queue.appendleft(queue.pop())
                mv += 1


if __name__ == "__main__":
    run()
