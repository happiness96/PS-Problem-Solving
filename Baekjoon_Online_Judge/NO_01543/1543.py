# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 14                             | #
# | 1543 문서 검색                      | #
# -------------------------------------- #


if __name__ == "__main__":
    document = r_input().rstrip()
    find = r_input().rstrip()

    print(document.count(find))
