# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 23                   | #
# | 숫자 골라내기              | #
# ---------------------------- #


def run():
    T = int(r_input())

    for testcase in range(1, T + 1):
        N = int(r_input())

        num_cnt = {}

        for num in map(int, r_input().split()):
            num_cnt[num] = num_cnt.get(num, 0) + 1
        
        res = -1
        for num, cnt in num_cnt.items():
            if cnt % 2:
                if res < 0:
                    res = num
                
                else:
                    res ^= num

        print('Case #' + str(testcase))
        print(0 if res == -1 else res)


if __name__ == "__main__":
    run()
