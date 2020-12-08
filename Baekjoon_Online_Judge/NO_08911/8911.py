# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 08                             | #
# | 8911 거북이                         | #
# -------------------------------------- #


def run():
    T = int(r_input())
    mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for _ in range(T):
        move = r_input().rstrip()
        way = 0

        min_row, max_row = 500, 500
        min_col, max_col = 500, 500
        row, col = 500, 500

        for m in move:
            if m == 'F':
                mv_row, mv_col = mv[way]

                row += mv_row
                col += mv_col

                min_row = min(row, min_row)
                min_col = min(col, min_col)
                max_row = max(row, max_row)
                max_col = max(col, max_col)
            
            elif m == 'B':
                mv_row, mv_col = mv[(way + 2) % 4]

                row += mv_row
                col += mv_col

                min_row = min(row, min_row)
                min_col = min(col, min_col)
                max_row = max(row, max_row)
                max_col = max(col, max_col)
            
            elif m == 'L':
                way -= 1

                if way == -1:
                    way = 3
            
            else:
                way += 1

                if way == 4:
                    way = 0
        
        print((max_row - min_row) * (max_col - min_col))


if __name__ == "__main__":
    run()
