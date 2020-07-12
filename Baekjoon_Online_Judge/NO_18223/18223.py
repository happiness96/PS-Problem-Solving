# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 12                   | #
# | 18223 민준이와 마산 그리고 건우| #
# ---------------------------- #


def run():
    INF = sys.maxsize
    V, E, P = map(int, r_input().split())

    con = {}

    for _ in range(E):
        a, b, c = map(int, r_input().split())

        if a not in con:
            con[a] = {}
        
        if b not in con:
            con[b] = {}
        
        if a not in con[b]:
            con[b][a] = INF
        
        if b not in con[a]:
            con[a][b] = INF

        con[a][b] = min(con[a][b], c)
        con[b][a] = min(con[b][a], c)
    
    if P in (1, V):
        print('SAVE HIM')
        sys.exit()

    queue = []
    dist = [INF] * (V + 1)
    visit = [0] * (V + 1)
    visit[1] = 1

    for con_node in con[1]:
        queue.append((con[1][con_node], con_node))
        dist[con_node] = con[1][con_node]
    
    heapify(queue)

    while queue:
        min_dist, min_node = heappop(queue)
        visit[min_node] = 1

        for con_node in con[min_node]:
            if not visit[con_node]:
                tmp_dist = min_dist + con[min_node][con_node]

                if tmp_dist < dist[con_node]:
                    heappush(queue, (tmp_dist, con_node))
                    dist[con_node] = tmp_dist
    
    queue2 = []
    dist2 = [INF] * (V +1)
    visit2 = [0] * (V + 1)
    visit2[P] = 1

    for con_node in con[P]:
        queue2.append((con[P][con_node], con_node))
        dist2[con_node] = con[P][con_node]
    
    heapify(queue2)

    while queue2:
        min_dist, min_node = heappop(queue2)
        visit2[min_node] = 1

        for con_node in con[min_node]:
            if not visit2[con_node]:
                tmp_dist = min_dist + con[min_node][con_node]

                if tmp_dist < dist2[con_node]:
                    heappush(queue2, (tmp_dist, con_node))
                    dist2[con_node] = tmp_dist
    
    if dist[-1] == dist[P] + dist2[-1]:
        print('SAVE HIM')
    
    else:
        print('GOOD BYE')


if __name__ == "__main__":
    run()
