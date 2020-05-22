# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 21                   | #
# | 3995 스네이크 큐브        | #
# ---------------------------- #


def cube_stake(height, row, col, alphabet, direction):
    snake_cube[height][row][col] = alphabet

    if alphabet == 'N':
        for snake_height in snake_cube:
            for ind, snake_row in enumerate(snake_height):
                print(snake_row[0] + snake_row[1] + snake_row[2], end='')

                if ind != 2:
                    print(' ', end='')
            print()
        
        sys.exit()

    next_alphabet = alpha[alpha.index(alphabet) + 1]

    flag = 1        # 꺾이는 구간인지 확인

    if alphabet != 'A':
        pre_alphabet = alpha[alpha.index(alphabet) - 1]

        pre_row, pre_col = cube_location[pre_alphabet]
        cur_row, cur_col = cube_location[alphabet]
        next_row, next_col = cube_location[next_alphabet]

        if pre_row - cur_row != cur_row - next_row or pre_col - cur_col != cur_col - next_col:
            flag = 0
    
    if flag:
        mv_height, mv_row, mv_col = mv[direction]
        tmp_height = height + mv_height
        tmp_row = row + mv_row
        tmp_col = col + mv_col
        
        if 0 <= tmp_height < 3 and 0 <= tmp_row < 3 and 0 <= tmp_col < 3:
            if snake_cube[tmp_height][tmp_row][tmp_col] == '0':
                cube_stake(tmp_height, tmp_row, tmp_col, next_alphabet, direction)

    else:
        for ind, move in enumerate(mv):
            if ind == direction:
                continue

            mv_height, mv_row, mv_col = move
            tmp_height = height + mv_height
            tmp_row = row + mv_row
            tmp_col = col + mv_col

            if 0 <= tmp_height < 3 and 0 <= tmp_row < 3 and 0 <= tmp_col < 3:
                if snake_cube[tmp_height][tmp_row][tmp_col] == '0':
                    cube_stake(tmp_height, tmp_row, tmp_col, next_alphabet, ind)
    
    snake_cube[height][row][col] = '0'
                    

if __name__ == "__main__":
    alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmN'

    cube_location = {}

    for row in range(15):
        line = r_input().rstrip()

        for col in range(15):
            if line[col] != '.':
                cube_location[line[col]] = (row, col)
    
    mv = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [-0, 0, -1], [0, 0, 1]]

    snake_cube = [[['0' for _ in range(3)] for _ in range(3)] for _ in range(3)]
    cube_stake(0, 0, 0, 'A', 1)
    cube_stake(1, 1, 0, 'A', 1)
    cube_stake(1, 1, 0, 'A', 5)
