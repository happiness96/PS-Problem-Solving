# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 27                             | #
# | 1022 소용돌이 예쁘게 출력하기       | #
# -------------------------------------- #


def chk(r, c, n):
    global max_length

    if r in res:
        if c in res[r]:
            res[r][c] = n
            max_length = max(max_length, len(str(n)))


if __name__ == "__main__":
    r1, c1, r2, c2 = map(int, r_input().split())

    res = {row: {col: 0 for col in range(c1, c2 + 1)} for row in range(r1, r2 + 1)}
    max_length = 0

    number = level = 1
    row, col = 0, 0

    chk(row, col, number)
    number += 1
    col += 1
    
    for lv in range(1, max(abs(r1), abs(r2), abs(c1), abs(c2)) + 1):
        for _ in range(2 * lv - 1):
            chk(row, col, number)
            row -= 1
            number += 1

        for _ in range(2 * lv):
            chk(row, col, number)
            col -= 1
            number += 1
        
        for _ in range(2 * lv):
            chk(row, col, number)
            row += 1
            number += 1
        
        for _ in range(2 * lv + 1):
            chk(row, col, number)
            col += 1
            number += 1
    

    for r in res:
        res_list = []

        for val in res[r].values():
            res_list.append(' ' * (max_length - len(str(val))) + str(val))
        
        print(*res_list)
