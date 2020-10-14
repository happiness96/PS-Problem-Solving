# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 14                             | #
# | 1895 필터                           | #
# -------------------------------------- #


def run():
    R, C = map(int, r_input().split())

    img = [list(map(int, r_input().split())) for _ in range(R)]
    T = int(r_input())
    res = 0

    for row in  range(R - 2):
        for col in range(C - 2):
            save = []

            for k in range(3):
                save += img[row + k][col: col + 3]
            
            res += int(sorted(save)[4] >= T)
    
    print(res)


if __name__ == "__main__":
    run()
