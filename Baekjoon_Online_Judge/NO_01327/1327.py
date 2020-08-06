# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 05                   | #
# | 1327 소트 게임             | #
# ---------------------------- #


def run():
    N, K = map(int, r_input().split())

    arr = list(map(int, r_input().split()))
    vis = []
    vis.append(arr)

    res = sorted(arr)

    queue = deque([arr])
    move = 0

    while queue:
        for _ in range(len(queue)):
            tmp = queue.popleft()

            if tmp == res:
                print(move)
                sys.exit()
            
            for ind in range(N - K + 1):
                aft = tmp[:ind] + tmp[ind: ind + K][::-1] + tmp[ind + K:]

                if aft not in vis:
                    vis.append(aft)
                    queue.append(aft)
        
        move += 1
    
    print(-1)


if __name__ == "__main__":
    run()
