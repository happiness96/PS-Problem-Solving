# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 01                   | #
# | 17352 여러분의 다리가 되어 드리겠습니다!| #
# ---------------------------- #


def run():
    N = int(r_input())

    visit = [0] * (N + 1)

    con = {node: [] for node in range(1, N + 1)}

    for _ in range(N - 2):
        a, b = map(int, r_input().split())

        con[a].append(b)
        con[b].append(a)
    
    if not con[1]:
        print(1, 2)
    
    else:
        queue = [1]
        visit[1] = 1

        while queue:
            node = queue.pop()

            for con_node in con[node]:
                if not visit[con_node]:
                    visit[con_node] = 1
                    queue.append(con_node)
        
        for ind in range(1, N + 1):
            if visit[ind]:
                print(ind, end=' ')
                break
        
        for ind in range(1, N + 1):
            if not visit[ind]:
                print(ind)
                break


if __name__ == "__main__":
    run()
