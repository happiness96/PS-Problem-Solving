# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 11                             | #
# | 3987 보이저 1호                     | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())
    board = [list(r_input().rstrip()) for _ in range(N)]

    PR, PC = map(int, r_input().split())
    PR -= 1
    PC -= 1

    mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    res = []

    for ind in range(4):
        time = 0
        direction = ind
        row, col = PR, PC

        visit = set()
        
        while True:
            if not 0 <= row < N or not 0 <= col < M:
                break

            if (row, col, direction) in visit:
                print('URDL'[ind])
                print('Voyager')
                sys.exit()
            
            visit.add((row, col, direction))

            val = board[row][col]

            if val == 'C':
                break
        
            elif val == '/':
                direction = [1, 0, 3, 2][direction]
            
            elif val == '\\':
                direction = [3, 2, 1, 0][direction]
            
            mv_row, mv_col = mv[direction]
            row += mv_row
            col += mv_col

            time += 1
        
        res.append(time)
    
    print('URDL'[res.index(max(res))])
    print(max(res))


if __name__ == "__main__":
    run()
