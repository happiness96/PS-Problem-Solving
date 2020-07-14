# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 14                   | #
# | 14659 한조서열정리하고옴ㅋㅋ | #
# ---------------------------- #


def run():
    N = int(r_input())
    max_height = 0
    result = 0
    cnt = 0

    for height in map(int, r_input().split()):
        if height > max_height:
            max_height = height
            result = max(result, cnt)
            cnt = 0
        
        else:
            cnt += 1
    
    print(max(result, cnt))


if __name__ == "__main__":
    run()
