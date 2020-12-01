# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 01                             | #
# | 17205 진우의 비밀번호               | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    pw = r_input().rstrip()

    save = [1]

    for _ in range(N - 1):
        save.append(save[-1] * 26)
    
    for i in range(1, N):
        save[i] += save[i - 1]

    save = save[::-1]
    
    tot = len(pw)
    for ind, ch in enumerate(pw):
        tot += save[ind] * (ord(ch) - 97)

    print(tot)
