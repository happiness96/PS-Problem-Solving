# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 22                             | #
# | 19843 수면 패턴                    | #
# -------------------------------------- #


if __name__ == "__main__":
    T, N = map(int, r_input().split())

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    sleep_time = 0

    for _ in range(N):
        D1, H1, D2, H2 = map(str, r_input().rstrip().split())

        H1 = int(H1)
        H2 = int(H2)

        sleep_time += (24 * days.index(D2) + H2) - (24 * days.index(D1) + H1)

    T -= sleep_time

    if T > 48:
        print(-1)
    
    else:
        print(max(T, 0))
