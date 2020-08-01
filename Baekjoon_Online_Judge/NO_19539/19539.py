# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 01                   | #
# | 19539 사과나무             | #
# ---------------------------- #


def run():
    N = int(r_input())

    one = 0
    two = 0

    for h in map(int, r_input().split()):
        one += h % 2
        two += h // 2
    
    print('NO' if one > two or (two - one) % 3 else 'YES')


if __name__ == "__main__":
    run()
