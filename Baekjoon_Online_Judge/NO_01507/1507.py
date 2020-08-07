# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 07                             | #
# | 1507 궁금한 민호                    | #
# -------------------------------------- #


def run():
    N = int(r_input())

    queue = []

    for A in range(N):
        tmp = list(map(int, r_input().split()))

        for B in range(A + 1, N):
            queue.append((tmp[B], (A, B)))
        
    queue.sort(reverse=True)

    INF = sys.maxsize
    dist = [[INF] * N for _ in range(N)]
    result = 0

    while queue:
        cost, start_dest = queue.pop()
        start, dest = start_dest

        if dist[start][dest] < cost:
            print(-1)
            sys.exit()

        if dist[start][dest] == cost:
            continue

        result += cost

        dist[start][dest] = cost
        dist[dest][start] = cost

        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp_dist = dist[k][i] + dist[i][j]

                    if tmp_dist < dist[k][j]:
                        dist[k][j] = tmp_dist
                        dist[j][k] = tmp_dist
        
    print(result)


if __name__ == "__main__":
    run()
