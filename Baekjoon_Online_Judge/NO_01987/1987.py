# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 15                             | #
# | 1987 알파벳                         | #
# -------------------------------------- #


def run():
    R, C = map(int, r_input().split())

    board = [list(r_input().rstrip()) for _ in range(R)]

    mv = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    res = 0

    queue = deque([[0, 0, [board[0][0]]]])

    while queue:
        new_queue = set()
        res += 1

        tmp = set()

        for _ in range(len(queue)):
            row, col, check_list = queue.popleft()

            for mv_row, mv_col in mv:
                tmp_row = row + mv_row
                tmp_col = col + mv_col

                if 0 <= tmp_row < R and 0 <= tmp_col < C:
                    if board[tmp_row][tmp_col] not in check_list:
                        new_check_list = list(check_list) + [board[tmp_row][tmp_col]]
                        new_check_list.sort()

                        new_queue.add((tmp_row, tmp_col, tuple(new_check_list)))
                
            tmp.add((row, col))
        
        queue = deque(new_queue)

    print(res)


if __name__ == "__main__":
    run()
