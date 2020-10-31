# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 31                             | #
# | 18229 내가 살게, 아냐 내가 살게     | #
# -------------------------------------- #


def run():
    N, M, K = map(int, r_input().split())

    who_charge = 0
    min_cnt = sys.maxsize

    for no in range(1, N + 1):
        A = list(map(int, r_input().split()))

        tot = 0

        for ind, val in enumerate(A):
            tot += val

            if tot >= K:
                if ind < min_cnt:
                    min_cnt = ind
                    who_charge = no
                
                break
    
    print(who_charge, min_cnt + 1)


if __name__ == "__main__":
    run()
