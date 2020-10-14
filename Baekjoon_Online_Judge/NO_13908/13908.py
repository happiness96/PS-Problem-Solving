# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 14                             | #
# | 13908 비밀번호                      | #
# -------------------------------------- #


def run():
    n, m = map(int, r_input().split())
    known = list(map(str, r_input().rstrip().split()))

    res = 0

    for pw in range(10 ** n):
        flag = 1
        str_pw = '0' * (n - len(str(pw))) + str(pw)

        for k in known:
            if k not in str_pw:
                flag = 0
                break
    
        res += flag
    
    print(res)


if __name__ == "__main__":
    run()
