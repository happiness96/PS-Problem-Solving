# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 02                   | #
# | 1138 한 줄로 서기          | #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    taller = list(map(int, r_input().split()))
    res = list(range(1, N + 1))

    for ind in range(N - 1, 0, -1):
        mv = taller[ind - 1]

        p_ind = res.pop(res.index(ind))
        res.insert(p_ind + mv - 1, ind)
        
    print(*res)
