# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 29                             | #
# | 9715 면적 구하기                     | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        R, C = map(int, r_input().split())

        board = [[0] * (C + 2)]
        res = 0

        for _ in range(R):
            line = [0] + list(map(int, list(r_input().rstrip()))) + [0]
            board.append(line)
        
        board.append([0] * (C + 2))

        for row in range(1, R + 1):
            for col in range(1, C + 1):
                block = board[row][col]

                for mv_row, mv_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    tmp_row = row + mv_row
                    tmp_col = col + mv_col

                    res += max(0, block - board[tmp_row][tmp_col])
                
                res += int(block != 0) * 2
        
        print(res)


if __name__ == "__main__":
    run()
