# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 13                             | #
# | 10649 사이 나쁜 여왕들              | #
# -------------------------------------- #


if __name__ == "__main__":
    board = []
    flag = 1
    queens = []

    for row in range(8):
        line = r_input().rstrip()
        
        if line.count('*') != 1:
            flag = 0

        for col in range(8):
            if line[col] == '*':
                queens.append((row, col))
        
        board.append(list(line))

    for col in range(8):
        cnt = 0
        for row in range(8):
            if board[row][col] == '*':
                cnt += 1
        
        if cnt != 1:
            flag = 0
            break

    queens_cnt = len(queens)

    for ind1 in range(queens_cnt):
        for ind2 in range(ind1 + 1, queens_cnt):
            q1_row, q1_col = queens[ind1]
            q2_row, q2_col = queens[ind2]

            if abs(q1_row - q2_row) == abs(q1_col - q2_col):
                flag = 0
                break
        
        if not flag:
            break
    
    print(['invalid', 'valid'][flag])
