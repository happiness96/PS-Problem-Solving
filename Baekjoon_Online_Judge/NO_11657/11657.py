# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 12                             | #
# | 11657 타임머신                     | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())
    INF = sys.maxsize

    dist = [INF] * (N + 1)
    edge = {node: {} for node in range(1, N + 1)}

    dist[1] = 0

    for _ in range(M):
        A, B, C = map(int, r_input().split())
        edge[A][B] = min(edge[A].get(B, INF), C)
    
    for turn in range(N + 1):
        for start_node in edge:
            for dest_node, val in edge[start_node].items():
                if dist[start_node] == INF:
                    continue

                tmp_dist = dist[start_node] + val

                if tmp_dist < dist[dest_node]:
                    if turn == N:
                        print(-1)
                        sys.exit()
                    
                    dist[dest_node] = tmp_dist
            
    for val in dist[2:]:
        if val == INF:
            print(-1)
        
        else:
            print(val)


if __name__ == "__main__":
    run()
