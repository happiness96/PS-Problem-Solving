# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 31                             | #
# | 알람 시계                          | #
# -------------------------------------- #


if __name__ == "__main__":
    H, M = map(int, r_input().split())

    # 45분 앞서는 시간으로 바꾼다.
    M -= 45

    # 분(M)이 음수가 될 경우 시(H)를 감소시켜준 후 60분을 더한다.
    if M < 0:
        M += 60
        H -= 1

    # 시(H)가 음수가 된 경우 24시를 더한다.
    if H < 0:
        H += 24

    print(H, M)
