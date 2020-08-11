# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 11                             | #
# | 1260 DFS와 BFS                     | #
# -------------------------------------- #


def DFS(node):
    print(node, end=' ')

    for con_node in sorted(con[node]):
        if not visit[con_node]:
            visit[con_node] = 1
            DFS(con_node)


def BFS():
    queue = deque([V])

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for con_node in sorted(con[node]):
            if not visit[con_node]:
                visit[con_node] = 1
                queue.append(con_node)


if __name__ == "__main__":
    N, M, V = map(int, r_input().split())

    con = {node: set() for node in range(N + 1)}

    for _ in range(M):
        A, B = map(int, r_input().split())
        
        con[A].add(B)
        con[B].add(A)

    visit = [0] * (N + 1)
    visit[V] = 1
    DFS(V)
    print()
    visit = [0] * (N + 1)
    visit[V] = 1
    BFS()
