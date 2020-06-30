# -*- encoding: utf-8 -*-
import sys
from collections import deque
from copy import deepcopy
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 30                   | #
# | 19236 청소년 상어         | #
# ---------------------------- #


def run():
    init_board = []
    init_fish_loc = {}

    for row in range(4):
        line = list(map(int, r_input().split()))
        save = []

        for col in range(4):
            save.append([line[2 * col], line[2 * col + 1]])

            init_fish_loc[line[2 * col]] = (row, col)

        init_board.append(save)
    
    result = 0

    init_shark_loc = (0, 0)
    init_shark_dir = init_board[0][0][1]
    init_total = init_board[0][0][0]

    init_fish_loc.pop(init_board[0][0][0])
    init_board[0][0] = [0, 0]

    queue = deque([[init_board, init_fish_loc, init_shark_loc, init_shark_dir, init_total]])

    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

    while queue:
        board, fish_loc, shark_loc, shark_dir, total = queue.popleft()

        for no in range(1, 17):
            if no in fish_loc:
                row, col = fish_loc[no]
                fish_dir = board[row][col][1]
                
                while True:
                    mv_row = row + dx[fish_dir]
                    mv_col = col + dy[fish_dir]

                    if 0 <= mv_row < 4 and 0 <= mv_col < 4:
                        if (mv_row, mv_col) != shark_loc:
                            tmp_no = board[mv_row][mv_col][0]
                            board[row][col][1] = fish_dir

                            if tmp_no:
                                fish_loc[tmp_no] = (row, col)
                            
                            fish_loc[no] = (mv_row, mv_col)
                            board[row][col], board[mv_row][mv_col] = board[mv_row][mv_col], board[row][col]
                            break
                    
                    fish_dir +=1
                    
                    if fish_dir == 9:
                        fish_dir = 1
        
        flag = 0

        for mv in range(1, 4):
            row, col = shark_loc

            mv_row = row + dx[shark_dir] * mv
            mv_col = col + dy[shark_dir] * mv

            if 0 <= mv_row < 4 and 0 <= mv_col < 4:
                if board[mv_row][mv_col] != [0, 0]:
                    flag = 1
                    copy_board = deepcopy(board)
                    copy_fish_loc = deepcopy(fish_loc)

                    eat, aft_dir = copy_board[mv_row][mv_col]

                    copy_fish_loc.pop(eat)
                    copy_board[mv_row][mv_col] = [0, 0]
                    
                    queue.append([copy_board, copy_fish_loc, (mv_row, mv_col), aft_dir, total + eat])

            else:
                break
        
        if not flag:
            result = max(result, total)

    print(result)


if __name__ == "__main__":
    run()
