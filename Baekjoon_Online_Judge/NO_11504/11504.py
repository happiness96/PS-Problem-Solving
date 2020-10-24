# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 24                             | #
# | 11504 돌려 돌려 돌림판!             | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        N, M = map(int, r_input().split())

        X = int(''.join(map(str, r_input().rstrip().split())))
        Y = int(''.join(map(str, r_input().rstrip().split())))

        board = list(map(str, r_input().rstrip().split()))

        board += board[: M]

        res = 0

        for ind in range(N):
            tmp_num = int(''.join(board[ind: ind + M]))
            
            if X <= tmp_num <= Y:
                res += 1
            
        print(res)
