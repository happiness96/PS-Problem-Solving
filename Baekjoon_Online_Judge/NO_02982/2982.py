# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 26                             | #
# | 2982 국왕의 방문                    | #
# -------------------------------------- #


def run():
    INF = sys.maxsize
    N, M = map(int, r_input().split())

    A, B, K, G = map(int, r_input().split())

    godula = list(map(int, r_input().split()))
    dist = {node: {} for node in range(1, N + 1)}

    for _ in range(M):
        U, V, L = map(int, r_input().split())
        dist[U][V] = min(dist[U].get(V, INF), L)
        dist[V][U] = min(dist[V].get(U, INF), L)
    
    godula_time = {}

    start_time = 0
    for ind in range(G - 1):
        start, end = godula[ind], godula[ind + 1]
        
        end_time = start_time + dist[start][end]
        godula_time[(start, end)] = (start_time, end_time)
        godula_time[(end, start)] = (start_time, end_time)

        start_time = end_time
    
    dijkstra_dist = [INF] * (N + 1)
    visit = [0] * (N + 1)
    queue = []

    visit[A] = 1
    for node, val in dist[A].items():
        if (A, node) in godula_time:
            start_time, end_time = godula_time[(A, node)]

            if start_time <= K < end_time:
                dijkstra_dist[node] = end_time + val
                queue.append((end_time + val, node))
                continue
        
        dijkstra_dist[node] = K + val
        queue.append((K + val, node))
    
    heapify(queue)
    
    while queue:
        cur_time, node = heappop(queue)
        visit[node] = 1

        for con_node, val in dist[node].items():
            if not visit[con_node]:
                tmp_time = cur_time + val

                if (node, con_node) in godula_time:
                    start_time, end_time = godula_time[(node, con_node)]

                    if start_time <= cur_time < end_time:
                        tmp_time = end_time + val
                
                if tmp_time < dijkstra_dist[con_node]:
                    dijkstra_dist[con_node] = tmp_time
                    heappush(queue, (tmp_time, con_node))

    print(dijkstra_dist[B] - K)


if __name__ == "__main__":
    run()
