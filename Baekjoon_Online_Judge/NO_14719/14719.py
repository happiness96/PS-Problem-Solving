# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 30                   | #
# | 14719 빗물                | #
# ---------------------------- #


if __name__ == "__main__":
    H, W = map(int, r_input().split())

    blocks = list(map(int, r_input().split()))
    left = 0
    save = []
    result = 0

    for height in blocks:
        if height >= left:
            for s in save:
                result += left - s
            
            left = height
            save = []
        
        else:
            save.append(height)

            for ind, val in enumerate(save):
                if val < height:
                    result += height - val
                    save[ind] = height
    
    print(result)
