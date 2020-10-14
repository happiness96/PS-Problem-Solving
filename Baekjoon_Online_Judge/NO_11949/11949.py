# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 14                             | #
# | 11949 번호표 교환                   | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    number_ticket = [int(r_input()) for _ in range(N)]

    for card_number in range(2, M + 1):
        for ind in range(N - 1):
            if number_ticket[ind] % card_number > number_ticket[ind + 1] % card_number:
                number_ticket[ind], number_ticket[ind + 1] = number_ticket[ind + 1], number_ticket[ind]
    
    print(*number_ticket, sep='\n')
