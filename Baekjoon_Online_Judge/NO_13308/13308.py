# -*- encoding: utf-8 -*-
import sys
from collections import deque
from heapq import *
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 02                   | #
# | 13308 주유소              | #
# ---------------------------- #


def run():
    INF = sys.maxsize

    N, M = map(int, r_input().split())
    price_per_liter = [0] + list(map(int, r_input().split()))

    dist = {node: {} for node in range(1, N + 1)}

    for _ in range(M):
        A, B, C = map(int, r_input().split())

        dist[A][B] = min(C, dist[A].get(B, INF))
        dist[B][A] = min(C, dist[B].get(A, INF))
    
    dijkstra_dist = [[INF] * (N + 1)]

    for start in range(1, N + 1):
        save = [INF] * (N + 1)
        save[start] = 0

        visit = [0] * (N + 1)
        queue = []

        heappush(queue, (0, start))

        while queue:
            val, node = heappop(queue)
            visit[node] = 1

            for con_node, plus in dist[node].items():
                if not visit[con_node]:
                    tmp_val = val + plus

                    if tmp_val < save[con_node]:
                        save[con_node] = tmp_val
                        heappush(queue, (tmp_val, con_node))
        
        dijkstra_dist.append(save)
    
    # from_to = {node: [] for node in range(1, N + 1 )}
    min_cost = [INF] * (N + 1)
    min_cost[1] = 0
    queue = []
    heappush(queue, [0, 1])

    while queue:
        tot_cost, start = heappop(queue)
        cost = price_per_liter[start]

        for dest in range(1, N + 1):
            if price_per_liter[dest] < cost:
                tmp_cost = tot_cost + dijkstra_dist[start][dest] * cost

                if tmp_cost < min_cost[dest]:
                    min_cost[dest] = tmp_cost
                    heappush(queue, [tmp_cost, dest])
            
            if dest == N:
                min_cost[dest] = min(min_cost[dest], tot_cost + dijkstra_dist[start][dest] * cost)
    
    print(min_cost[-1])


if __name__ == "__main__":
    run()
