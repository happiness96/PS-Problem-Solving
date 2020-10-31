# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 31                             | #
# | 2045 마방진                         | #
# -------------------------------------- #


def run():
    board = [list(map(int, r_input().split())) for _ in range(3)]

    if board[0][0] == board[1][1] == board[2][2] == 0:
        res = 0

        for b in board:
            res += sum(b)
        
        res //= 2

        for k in range(3):
            board[k][k] = res - sum(board[k])
        
        for b in board:
            print(*b)
        
    elif board[0][2] == board[1][1] == board[2][0] == 0:
        res = 0

        for b in board:
            res += sum(b)
        
        res //= 2

        board[0][2] = res - sum(board[0])
        board[1][1] = res - sum(board[1])
        board[2][0] = res - sum(board[2])

        for b in board:
            print(*b)

    else:
        max_sum = 0

        for b in board:
            max_sum = max(max_sum, sum(b))
        
        for col in range(3):
            tot = 0

            for row in range(3):
                tot += board[row][col]
            
            max_sum = max(max_sum, tot)
        
        tot = 0

        for k in range(3):
            tot += board[k][k]
        
        max_sum = max(max_sum, tot)

        tot = 0
        
        for k in range(3):
            tot += board[2 - k][k]
        
        max_sum = max(max_sum, tot)

        for row in range(3):
            if board[row].count(0) > 1:
                break

            if sum(board[row]) != max_sum:
                board[row][board[row].index(0)] = max_sum - sum(board[row])
        
        for col in range(3):
            tot = 0

            for row in range(3):
                tot += board[row][col]
            
            if tot != max_sum:
                for row in range(3):
                    if not board[row][col]:
                        board[row][col] = max_sum - tot
                        break
        
        for b in board:
            print(*b)


if __name__ == "__main__":
    run()
