# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 28                             | #
# | 11726 2xn 타일링                    | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    save = [1, 1]

    for _ in range(1000):
        save.append((save[-1] + save[-2]) % 10007)
    
    print(save[n])
