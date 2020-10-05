# -*- encoding: utf-8 -*-
import sys
from itertools import permutations
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 05                             | #
# | 16985 Maaaaaaaaaze                 | #
# -------------------------------------- #


def make_cube(floor, rot, cube, order):
    global result

    if floor == 5:
        queue = deque([])

        if cube[0][0][0] == 1:
            queue.append((0, 0, 0))
        
        visit = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        visit[0][0][0] = 1
        distance = 0

        flag = 0
        
        while queue:
            for _ in range(len(queue)):
                h, r, c = queue.popleft()

                if h == r == c == 4:
                    if result == -1:
                        result = distance
                    
                    else:
                        result = min(result, distance)
                    
                    flag = 1
                    break
                
                for h_mv, r_mv, c_mv in mv:
                    tmp_h = h + h_mv
                    tmp_r = r + r_mv
                    tmp_c = c + c_mv

                    if 0 <= tmp_h < 5 and 0 <= tmp_r < 5 and 0 <= tmp_c < 5:
                        if not visit[tmp_h][tmp_r][tmp_c]:
                            visit[tmp_h][tmp_r][tmp_c] = 1

                            if cube[tmp_h][tmp_r][tmp_c] == 1:
                                queue.append((tmp_h, tmp_r, tmp_c))
            
            if flag:
                break
            
            distance += 1
    
    else:
        tmp_board = [[0] * 5 for _ in range(5)]
        ref_board = board[order[floor]]
        
        if rot == 0:
            for row in range(5):
                for col in range(5):
                    tmp_board[row][col] = ref_board[row][col]
        
        elif rot == 1:
            for row in range(5):
                for col in range(5):
                    tmp_board[row][col] = ref_board[col][4 - row]
            
        elif rot == 2:
            for row in range(5):
                for col in range(5):
                    tmp_board[row][col] = ref_board[4 - row][4 - col]
        
        else:
            for row in range(5):
                for col in range(5):
                    tmp_board[row][col] = ref_board[4 - col][row]
        
        cube.append(tmp_board)

        for m_r in range(4):
            make_cube(floor + 1, m_r, cube, order)
        
        cube.pop()


if __name__ == "__main__":
    board = [[list(map(int, r_input().split())) for _ in range(5)] for _ in range(5)]

    result = -1

    mv = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    
    for case in permutations(list(range(5)), 5):
        for r in range(4):
            make_cube(0, r, [], case)
        
        if board[0] == board[1] == board[2] == board[3] == board[4]:
            break
    
    print(result)
