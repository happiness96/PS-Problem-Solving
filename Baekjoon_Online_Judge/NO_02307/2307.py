# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 26                             | #
# | 2307 도로검문                        | #
# -------------------------------------- #


def run():
    INF = sys.maxsize
    N, M = map(int, r_input().split())

    dist = {node: {} for node in range(1, N + 1)}

    for _ in range(M):
        a, b, t = map(int, r_input().split())

        dist[a][b] = t
        dist[b][a] = t
    
    queue = []
    dijk_dist = [INF] * (N + 1)
    visit = [0] * (N + 1)
    min_path = []

    for con_node, val in dist[1].items():
        queue.append((val, con_node, [1, con_node]))
        dijk_dist[con_node] = val

        if con_node == N:
            min_path = [1, N]
    
    visit[1] = 1
    heapify(queue)

    while queue:
        val, node, cur_path = heappop(queue)
        visit[node] = 1

        for con_node, con_val in dist[node].items():
            if not visit[con_node]:
                tmp_val = val + con_val

                if tmp_val < dijk_dist[con_node]:
                    dijk_dist[con_node] = tmp_val
                    heappush(queue, (tmp_val, con_node, cur_path + [con_node]))

                    if con_node == N:
                        min_path = cur_path + [con_node]
    
    min_dist = dijk_dist[-1]
    res = 0

    for ind in range(len(min_path) - 1):
        first_node = min_path[ind]
        second_node = min_path[ind + 1]

        save_dist = dist[first_node][second_node]
        dist[first_node][second_node] = INF
        dist[second_node][first_node] = INF

        queue = []
        dijk_dist = [INF] * (N + 1)
        visit = [0] * (N + 1)

        for con_node, val in dist[1].items():
            queue.append((val, con_node))
            dijk_dist[con_node] = val
        
        visit[1] = 1
        heapify(queue)

        while queue:
            val, node = heappop(queue)
            visit[node] = 1

            for con_node, con_val in dist[node].items():
                if not visit[con_node]:
                    tmp_val = val + con_val

                    if tmp_val < dijk_dist[con_node]:
                        dijk_dist[con_node] = tmp_val
                        heappush(queue, (tmp_val, con_node))
        
        tmp_dist = dijk_dist[-1]
        
        if tmp_dist == INF:
            print(-1)
            sys.exit()
        
        res = max(res, tmp_dist - min_dist)
        dist[first_node][second_node] = save_dist
        dist[second_node][first_node] = save_dist
    
    print(res)


if __name__ == "__main__":
    run()
