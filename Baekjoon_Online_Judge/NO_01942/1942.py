# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 21                             | #
# | 1942 디지털시계                    | #
# -------------------------------------- #


def run():
    for _ in range(3):
        start, finish = map(str, r_input().rstrip().split())

        s_h, s_m, s_s = map(int, start.split(':'))
        f_h, f_m, f_s = map(int, finish.split(':'))

        start = s_h * 10000 + s_m * 100 + s_s
        finish = f_h * 10000 + f_m * 100 + f_s

        result = 0

        if start > finish:
            for h in range(24):
                for m in range(60):
                    for s in range(60):
                        cur = int("%02d%02d%02d" % (h, m, s))

                        if start <= cur or cur <= finish:
                            if cur % 3 == 0:
                                result += 1
        
        else:
            for h in range(24):
                for m in range(60):
                    for s in range(60):
                        cur = int("%02d%02d%02d" % (h, m, s))

                        if start <= cur <= finish:
                            if cur % 3 == 0:
                                result += 1
        
        print(result)


if __name__ == "__main__":
    run()
