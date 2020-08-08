# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 08                             | #
# | 2875 대회 or 인턴                  | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M, K = map(int, r_input().split())
    
    make_team = min(N // 2, M)

    rem = (N + M) - (3 * make_team)
    rem -= K

    if rem >= 0:
        print(make_team)
    
    else:
        rem = -rem

        div, mod = divmod(rem, 3)
        
        print(make_team - div - int(mod != 0))
