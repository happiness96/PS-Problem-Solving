# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 13                             | #
# | 1865 웜홀                          | #
# -------------------------------------- #


def run():
    TC = int(r_input())
    INF = sys.maxsize

    for _ in range(TC):
        N, M, W = map(int, r_input().split())

        dist = [[INF] * (N + 1) for _ in range(N + 1)]
        edge = {node: {} for node in range(1, N + 1)}
        visit = [0] * (N + 1)

        for _ in range(M):
            S, E, T = map(int, r_input().split())

            edge[S][E] = min(edge[S].get(E, INF), T)
            edge[E][S] = min(edge[E].get(S, INF), T)
        
        for _ in range(W):
            S, E, T = map(int, r_input().split())

            edge[S][E] = min(edge[S].get(E, INF), -T)
        
        flag = 1

        for node in range(1, N + 1):
            if visit[node]:
                continue

            visit[node] = 1
            dist[node][node] = 0

            for turn in range(N + 1):
                for start_node in edge:
                    for dest_node, val in edge[start_node].items():
                        if dist[node][start_node] == INF:
                            continue

                        tmp_dist = dist[node][start_node] + val

                        if tmp_dist < dist[node][dest_node]:
                            if turn == N:
                                flag = 0
                                break

                            dist[node][dest_node] = tmp_dist
                    
                    if not flag:
                        break
                
                if not flag:
                    break
            
            for con_node in range(1, N + 1):
                if dist[node][con_node] != INF:
                    visit[con_node] = 1
                    
            if not flag:
                break
        
        print(['YES', 'NO'][flag])


if __name__ == "__main__":
    run()
