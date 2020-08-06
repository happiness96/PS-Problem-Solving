# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 30                   | #
# | 2239 스도쿠               | #
# ---------------------------- #


def sudoku(row, col):
    if row == 9 and col == 0:
        for b in board:
            print(*b, sep='')
        
        sys.exit()
        
    next_row = row
    next_col = col + 1

    if next_col == 9:
        next_col = 0
        next_row += 1

    if board[row][col]:
        sudoku(next_row, next_col)
        return
    
    for number in range(1, 10):
        board[row][col] = number

        chk_row = 1
        chk_col = 1
        chk_box = 1

        for ind in range(9):
            if ind != col and board[row][ind] == number:
                chk_row = 0
                break
                
            if ind != row and board[ind][col] == number:
                chk_col = 0
                break
        
        if not chk_row or not chk_col:
            continue
    
        for start_x in range(3):
            for start_y in range(3):
                box = [0] * 10

                for x in range(start_x * 3, (start_x + 1) * 3):
                    for y in range(start_y * 3, (start_y + 1) * 3):
                        if board[x][y]:
                            box[board[x][y]] += 1
                
                if 2 in box:
                    chk_box = 0
                    break
            
            if not chk_box:
                break
        
        if chk_box:
            sudoku(next_row, next_col)
    
    board[row][col] = 0


if __name__ == "__main__":
    board = [list(map(int, list(r_input().rstrip()))) for _ in range(9)]

    sudoku(0, 0)
