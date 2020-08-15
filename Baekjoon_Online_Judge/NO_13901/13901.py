# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 15                             | #
# | 13901 로봇                         | #
# -------------------------------------- #


def run():
    R, C = map(int, r_input().split())
    k = int(r_input())

    obstacle = []

    for _ in range(k):
        br, bc = map(int, r_input().split())
        obstacle.append((br, bc))
    
    sr, sc = map(int, r_input().split())
    s_dir = 0
    direction = list(map(int, r_input().split()))
    visit = [[0] * C for _ in range(R)]
    visit[sr][sc] = 1

    mv = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        flag = 1

        for c in range(4):
            mv_r, mv_c = mv[direction[s_dir]]
            tmp_r, tmp_c = sr + mv_r, sc + mv_c

            if 0 <= tmp_r < R and 0 <= tmp_c < C:
                if not visit[tmp_r][tmp_c] and (tmp_r, tmp_c) not in obstacle:
                    visit[tmp_r][tmp_c] = 1
                    sr, sc = tmp_r, tmp_c
                    flag = 0
                    break
            
            s_dir += 1
            s_dir %= 4

        if flag:
            break
    
    print(sr, sc)


if __name__ == "__main__":
    run()
