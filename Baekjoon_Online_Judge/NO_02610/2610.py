# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 01                   | #
# | 2610 회의준비             | #
# ---------------------------- #


def run():
    N = int(r_input())
    M = int(r_input())

    INF = sys.maxsize

    con = {node: set() for node in range(1, N + 1)}
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, r_input().split())
        con[A].add(B)
        con[B].add(A)

        dist[A][B] = 1
        dist[B][A] = 1

    for i in range(N + 1):
        for j in range(N + 1):
            for k in range(N + 1):
                tmp = dist[k][i] + dist[i][j]
                
                if tmp < dist[k][j]:
                    dist[k][j] = tmp

    committee = []
    vis = [0] * (N + 1)

    for node in range(1, N + 1):
        if not vis[node]:
            queue = [node]
            people = [node]
            vis[node] = 1

            while queue:
                cur = queue.pop()

                for con_node in con[cur]:
                    if not vis[con_node]:
                        vis[con_node] = 1
                        queue.append(con_node)
                        people.append(con_node)
    
            committee.append(people)
    
    result = []

    for ind in range(1, N + 1):
        dist[ind][ind] = INF
    
    for people in committee:
        min_val = INF
        min_node = 0

        for node in people:
            maxi = 0

            for val in dist[node]:
                if val != INF:
                    maxi = max(maxi, val)
            
            if maxi < min_val:
                min_val = maxi
                min_node = node
        
        result.append(min_node)
    
    result.sort()
    print(len(result))
    print(*result, sep='\n')


if __name__ == "__main__":
    run()
