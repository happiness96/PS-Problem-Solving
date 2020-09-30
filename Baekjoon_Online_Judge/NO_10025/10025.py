# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 30                             | #
# | 10025 게으른 백곰                  | #
# -------------------------------------- #


def run():
    N, K = map(int, r_input().split())
    K = min(K * 2 + 1, 1000000)

    maxi = 0
    save = [0] * 1000001

    for _ in range(N):
        g, x = map(int, r_input().split())
        save[x] = g

        maxi = max(maxi, x)

    res = sum(save[:K])
    tmp = res
    
    for ind in range(K, maxi + 1):
        tmp -= save[ind - K]
        tmp += save[ind]

        res = max(res, tmp)
        
    print(res)


if __name__ == "__main__":
    run()
