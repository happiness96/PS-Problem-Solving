# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 13                             | #
# | 14607 피자 (Large)                 | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    
    save = {N: 1}
    res = 0

    while save:
        new_save = {}

        for num, cnt in save.items():
            if num == 1:
                continue

            div1 = num // 2
            div2 = num - div1

            res += (div1 * div2) * cnt

            if div1 not in new_save:
                new_save[div1] = 0
            
            if div2 not in new_save:
                new_save[div2] = 0

            new_save[div1] += cnt
            new_save[div2] += cnt
        
        save = new_save
    
    print(res)
