# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 28                   | #
# | 2890 카약                 | #
# ---------------------------- #


if __name__ == "__main__":
    R, C = map(int, r_input().split())

    res = [0] * 10
    rank = 1

    board = [list(r_input().rstrip()) for _ in range(R)]

    for col in range(C - 2, 0, -1):
        flag = 0

        for row in range(R):
            val = board[row][col]

            if val in '123456789':
                if not res[int(val)]:
                    flag = 1

                    res[int(val)] = rank
        
        rank += flag
    
    print(*res[1:], sep='\n')
