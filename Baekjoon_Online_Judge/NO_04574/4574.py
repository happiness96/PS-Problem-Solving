# -*- encoding: utf-8 -*-
import sys
from itertools import combinations
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 27                   | #
# | 4574 스도미노쿠            | #
# ---------------------------- #


def chk_puzzle_down(row, col):
    ck_list = [0] * 10

    for r in range(9):
        if puzzle[r][col]:
            ck_list[puzzle[r][col]] += 1
    
    if 2 in ck_list:
        return 0
    
    ck_list1 = [0] * 10
    ck_list2 = [0] * 10
    
    for c in range(9):
        if puzzle[row][c]:
            ck_list1[puzzle[row][c]] += 1
        
        if puzzle[row + 1][c]:
            ck_list2[puzzle[row + 1][c]] += 1
        
    if 2 in ck_list1 + ck_list2:
        return 0
    
    for i in range(3):
        for j in range(3):
            ck_list = [0] * 10

            for r in range(i * 3, (i + 1) * 3):
                for c in range(j * 3, (j + 1) * 3):
                    if puzzle[r][c]:
                        ck_list[puzzle[r][c]] += 1
            
            if 2 in ck_list:
                return 0
    
    return 1


def chk_puzzle_right(row, col):
    ck_list = [0] * 10

    for c in range(9):
        if puzzle[row][c]:
            ck_list[puzzle[row][c]] += 1
    
    if 2 in ck_list:
        return 0
    
    ck_list1 = [0] * 10
    ck_list2 = [0] * 10
    
    for r in range(9):
        if puzzle[r][col]:
            ck_list1[puzzle[r][col]] += 1
        
        if puzzle[r][col + 1]:
            ck_list2[puzzle[r][col + 1]] += 1
    
    if 2 in ck_list1 + ck_list2:
        return 0
    
    for i in range(3):
        for j in range(3):
            ck_list = [0] * 10

            for r in range(i * 3, (i + 1) * 3):
                for c in range(j * 3, (j + 1) * 3):
                    if puzzle[r][c]:
                        ck_list[puzzle[r][c]] += 1

            if 2 in ck_list:
                return 0
    
    return 1


def solve(row, col):
    global solved

    next_row = row
    next_col = col + 1

    if next_col == 9:
        next_col = 0
        next_row += 1

    if puzzle[row][col]:
        if row == col == 8:
            solved = 1
        
        else:
            solve(next_row, next_col)
        
        return
    
    down_to = 0
    right_to = 0

    if row != 8 and not puzzle[row + 1][col]:
        down_to = 1
    
    if col != 8 and not puzzle[row][col + 1]:
        right_to = 1
    
    if right_to:
        for case, val in domino.items():
            if val:
                continue
            
            domino[case] = 1
            puzzle[row][col] = case[0]
            puzzle[row][col + 1] = case[1]
            
            if chk_puzzle_right(row, col):
                solve(next_row, next_col)
            
            if solved:
                break
            
            puzzle[row][col] = case[1]
            puzzle[row][col + 1] = case[0]
            
            if chk_puzzle_right(row, col):
                solve(next_row, next_col)
            
            if solved:
                break

            domino[case] = 0
        
            puzzle[row][col] = 0
            puzzle[row][col + 1] = 0
    
    if down_to:
        for case, val in domino.items():
            if val:
                continue
            
            domino[case] = 1
            puzzle[row][col] = case[0]
            puzzle[row + 1][col] = case[1]
            
            if chk_puzzle_down(row, col):
                solve(next_row, next_col)
            
            if solved:
                break
            
            puzzle[row][col] = case[1]
            puzzle[row + 1][col] = case[0]

            if chk_puzzle_down(row, col):
                solve(next_row, next_col)
            
            if solved:
                break

            domino[case] = 0

            puzzle[row][col] = 0
            puzzle[row + 1][col] = 0


if __name__ == "__main__":
    alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
    puzzle_no = 1

    while True:
        N = int(r_input())

        if N == 0:
            break
        
        puzzle = [[0] * 9 for _ in range(9)]
        domino = {case: 0 for case in combinations(list(range(1, 10)), 2)}

        for _ in range(N):
            U, LU, V, LV = map(str, r_input().rstrip().split())
            U = int(U)
            V = int(V)

            puzzle[alphabet[LU[0]]][int(LU[1]) - 1] = U
            puzzle[alphabet[LV[0]]][int(LV[1]) - 1] = V

            if U > V:
                U, V = V, U
            
            domino[(U, V)] = 1

        locations = list(map(str, r_input().rstrip().split()))

        for ind, loc in enumerate(locations):
            puzzle[alphabet[loc[0]]][int(loc[1]) - 1] = ind + 1
        
        solved = 0
        solve(0, 0)

        print('Puzzle', puzzle_no)

        for p in puzzle:
            print(*p, sep='')
        
        puzzle_no += 1
