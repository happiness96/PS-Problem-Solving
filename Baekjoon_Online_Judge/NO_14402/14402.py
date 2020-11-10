# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 10                             | #
# | 14402 야근                          | #
# -------------------------------------- #


def run():
    q = int(r_input())

    save = {}
    over_night = 0

    for _ in range(q):
        s, p = map(str, r_input().rstrip().split())

        if p == '+':
            save[s] = save.get(s, 0) + 1
        
        else:
            if s in save and save[s]:
                save[s] -= 1
            
            else:
                over_night += 1
    
    print(sum(save.values()) + over_night)


if __name__ == "__main__":
    run()
