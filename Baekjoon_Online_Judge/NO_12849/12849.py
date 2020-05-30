# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 30                   | #
# | 12849 본대 산책           | #
# ---------------------------- #


def run():
    D = int(r_input())

    save = [0] * 8
    save[1] = 1
    save[2] = 1

    con = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [2, 3, 5, 7], [3, 4, 6], [5, 7], [4, 6]]

    for _ in range(D - 1):
        r_save = [0] * 8

        for ind, val in enumerate(save):
            if val:
                for connected in con[ind]:
                    r_save[connected] += val
                    r_save[connected] %= 1000000007
        
        save = r_save
    
    print(save[0])


if __name__ == "__main__":
    run()
