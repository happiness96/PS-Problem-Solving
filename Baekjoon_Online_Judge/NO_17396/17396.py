# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 12                             | #
# | 17396 백도어                        | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())
    sight = list(map(int, r_input().split()))
    sight[-1] = 0

    INF = sys.maxsize

    dist = {node: {} for node in range(N)}

    for _ in range(M):
        a, b, t = map(int, r_input().split())

        if sight[a] or sight[b]:
            dist[a][b] = INF
            dist[b][a] = INF
        
        else:
            dist[a][b] = t
            dist[b][a] = t

    dijk_dist = [INF] * N
    visit = [0] * N
    visit[-1] = 1

    queue = []

    for con, cost in dist[N - 1].items():
        queue.append((cost, con))
        dijk_dist[con] = cost
    
    heapify(queue)
    
    while queue:
        cost, node = heappop(queue)
        visit[node] = 1

        for con_node, con_cost in dist[node].items():
            if not visit[con_node]:
                tmp_cost = cost + con_cost

                if tmp_cost < dijk_dist[con_node]:
                    dijk_dist[con_node] = tmp_cost
                    heappush(queue, (tmp_cost, con_node))
    
    print(-1 if dijk_dist[0] == INF else dijk_dist[0])


if __name__ == "__main__":
    run()
