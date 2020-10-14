# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 14                             | #
# | 2116 주사위 쌓기                    | #
# -------------------------------------- #


def run():
    N = int(r_input())

    opposite_side = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
    dice = [list(map(int, r_input().split())) for _ in range(N)]

    result = 0

    for ind in range(6):
        tmp = 0

        up_ind = ind
        down_ind = opposite_side[ind]

        for dice_no in range(N):
            up_side = dice[dice_no][up_ind]
            down_side = dice[dice_no][down_ind]

            add = 6

            if 6 in (up_side, down_side):
                add -= 1

                if 5 in (up_side, down_side):
                    add -= 1
            
            tmp  += add

            if dice_no < N - 1:
                down_ind = dice[dice_no + 1].index(up_side)
                up_ind = opposite_side[down_ind]
        
        result = max(result, tmp)
    
    print(result)


if __name__ == "__main__":
    run()
