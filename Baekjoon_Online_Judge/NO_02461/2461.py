# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 12                             | #
# | 2461 대표 선수                       | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    status = [sorted(map(int, r_input().split())) for _ in range(N)]

    queue = []
    save = [0] * N

    for row in range(N):
        tmp = status[row][0]
        save[row] = tmp

        queue.append((tmp, row, 0))
    
    maxi = max(save)
    res = maxi - min(save)

    heapify(queue)

    while queue:
        val, row, col = heappop(queue)
        
        if col < M - 1:
            tmp = status[row][col + 1]
            save[row] = tmp

            queue.append((tmp, row, col + 1 ))

            maxi = max(maxi, tmp)
            res = min(res, maxi - min(save))
        
        if res == 0:
            break
        
    print(res)


if __name__ == "__main__":
    run()
