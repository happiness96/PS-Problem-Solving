# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 25                   | #
# | 2531 회전초밥              | #
# ---------------------------- #


def run():
    N, d, k, c = map(int, r_input().split())

    susi = [int(r_input()) for _ in range(N)]

    save = deque(susi[:k])

    result = len(set(save + deque([c])))

    for ind in range(k, N):
        save.popleft()
        save.append(susi[ind])

        result = max(result, len(set(save + deque([c]))))
    
    for ind in range(k):
        save.popleft()
        save.append(susi[ind])

        result = max(result, len(set(save + deque([c]))))
    
    print(result)
    

if __name__ == "__main__":
    run()
