# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 07                             | #
# | 2520 팬케이크 사랑                  | #
# -------------------------------------- #


if __name__ == "__main__":
    t = int(r_input())

    for _ in range(t):
        r_input()

        c, y, su, sa, f = map(int, r_input().split())
        b, gs, gc, w = map(int, r_input().split())

        dough_cnt = int(16 * min(c / 8, y / 8, su / 4, sa, f / 9))
        topping_cnt = b + gs // 30 + gc // 25 + w// 10

        print(min(dough_cnt, topping_cnt))
