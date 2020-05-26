# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 26                   | #
# | 15961 회전초밥            | #
# ---------------------------- #


def run():
    N, d, k, c = map(int, r_input().split())

    susi = [int(r_input()) for _ in range(N)]
    susi += susi[: k]
    save = [0] * (d + 1)

    result = 0

    for ind in range(k):
        val = susi[ind]

        if save[val] == 0:
            result += 1
        
        save[val] += 1
    
    if save[c] == 0:
        result += 1
    
    tot = result

    if save[c] == 0:
        tot -= 1

    for ind in range(k, N + k):
        rem = susi[ind - k]
        val = susi[ind]

        save[rem] -= 1

        if save[rem] == 0:
            tot -= 1
        
        if save[val] == 0:
            tot += 1
        
        save[val] += 1

        if save[c] == 0:
            result = max(result, tot + 1)
        
        else:
            result = max(result, tot)
    
    print(result)


if __name__ == "__main__":
    run()
