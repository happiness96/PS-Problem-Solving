# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 22                             | #
# | 10656 십자말 풀이                    | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    board = [['#' for _ in range(M + 3)]]

    for _ in range(N):
        board.append(['#'] + list(r_input().rstrip()) + ['#', '#'])
    
    for _ in range(2):
        board.append(['#' for _ in range(M + 3)])
    
    res = []
    
    for row in range(1, N + 1):
        for col in range(1, M + 1):
            if board[row - 1][col] == '#' and board[row][col] == board[row + 1][col] == board[row + 2][col] == '.':
                res.append((row, col))
            
            elif board[row][col - 1] == '#' and board[row][col] == board[row][col + 1] == board[row][col + 2] == '.':
                res.append((row, col))
    
    print(len(res))

    for r in res:
        print(*r)


if __name__ == "__main__":
    run()
