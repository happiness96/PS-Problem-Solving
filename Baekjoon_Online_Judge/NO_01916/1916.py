# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 06                             | #
# | 1916 최소비용 구하기                | #
# -------------------------------------- #


def run():
    INF = sys.maxsize
    N = int(r_input())
    M = int(r_input())

    dist = {start: {} for start in range(1, N + 1)}

    for _ in range(M):
        A, B, C = map(int, r_input().split())

        dist[A][B] = min(dist[A].get(B, INF), C)
    
    start, dest = map(int, r_input().split())

    dijk_dist = [INF] * (N + 1)
    visit = [0] * (N + 1)
    visit[start] = 1
    queue = []

    for to, cost in dist[start].items():
        dijk_dist[to] = cost
        queue.append((cost, to))
    
    heapify(queue)
    
    while queue:
        cost, node = heappop(queue)
        visit[node] = 1

        for con_node, val in dist[node].items():
            if not visit[con_node]:
                tmp_cost = cost + val

                if tmp_cost < dijk_dist[con_node]:
                    dijk_dist[con_node] = tmp_cost
                    heappush(queue, (tmp_cost, con_node))
    
    print(dijk_dist[dest])


if __name__ == "__main__":
    run()
