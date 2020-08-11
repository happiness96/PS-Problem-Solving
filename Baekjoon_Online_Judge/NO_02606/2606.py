# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 11                             | #
# | 2606 바이러스                      | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    M = int(r_input())

    con = {node: set() for node in range(1, N + 1)}

    for _ in range(M):
        A, B = map(int, r_input().split())

        con[A].add(B)
        con[B].add(A)
    
    queue = [1]
    visit = [0] * (N + 1)

    visit[1] = 1
    cnt = 0

    while queue:
        node = queue.pop()

        for con_node in con[node]:
            if not visit[con_node]:
                queue.append(con_node)
                visit[con_node] = 1
                cnt += 1
    
    print(cnt)
