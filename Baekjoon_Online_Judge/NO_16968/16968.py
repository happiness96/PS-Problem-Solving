# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 27                   | #
# | 16968 차량 번호판 1        | #
# ---------------------------- #


if __name__ == "__main__":
    form = r_input().rstrip()

    length = len(form)
    save = [0] * length

    for ind, val in enumerate(form):
        if val == 'd':
            save[ind] = 10
        
        else:
            save[ind] = 26
        
    for ind in range(length - 1):
        if save[ind] == save[ind + 1]:
            save[ind] -= 1
    
    res = 1

    for val in save:
        res *= val
    
    print(res)
