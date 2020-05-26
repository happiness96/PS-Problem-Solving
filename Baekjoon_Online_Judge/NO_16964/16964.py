# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 26                   | #
# | 16964 DFS 스페셜 저지      | #
# ---------------------------- #


def dfs(node):
    visit[node] = 1
    comp.popleft()

    rem = []

    for con in connected[node]:
        if not visit[con]:
            rem.append(con)
    
    while rem:
        if comp[0] in rem:
            dfs(rem.pop(rem.index(comp[0])))
    
        else:
            break


if __name__ == "__main__":
    N = int(r_input())

    connected = {node: [] for node in range(1, N + 1)}

    for _ in range(N - 1):
        A, B = map(int, r_input().split())

        connected[A].append(B)
        connected[B].append(A)
    
    comp = deque(map(int, r_input().split()))
    visit = [0] * (N + 1)

    dfs(1)

    print(int(comp == deque([])))
