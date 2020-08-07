# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 06                             | #
# | 19538 루머                          | #
# -------------------------------------- #


def run():
    N = int(r_input())

    trusted_rumor = [-1] * (N + 1)
    connected = {}
    trusted_cnt = [0] * (N + 1)

    for people_num in range(1, N + 1):
        *tmp, zero = map(int, r_input().split())
        connected[people_num] = tmp
    
    M = int(r_input())
    queue = deque(list(map(int, r_input().split())))
    time = 0

    for first_diffuser in queue:
        trusted_rumor[first_diffuser] = time

        for con in connected[first_diffuser]:
            trusted_cnt[con] += 1

    time += 1

    while queue:
        trusted = set()

        for _ in range(len(queue)):
            node = queue.popleft()

            for con_node in connected[node]:
                if trusted_rumor[con_node] == -1:
                    if trusted_cnt[con_node] >= len(connected[con_node]) / 2:
                        queue.append(con_node)
                        trusted.add(con_node)

        for trusted_node in trusted:
            trusted_rumor[trusted_node] = time

            for con in connected[trusted_node]:
                trusted_cnt[con] += 1
        
        time += 1
    
    print(' '.join(map(str, trusted_rumor[1:])))


if __name__ == "__main__":
    run()
