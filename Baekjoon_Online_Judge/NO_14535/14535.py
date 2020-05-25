# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 24                   | #
# | 14535 Birthday Graph     | #
# ---------------------------- #


if __name__ == "__main__":
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    testcase = 1

    while True:
        N = int(r_input())

        if N == 0:
            break
        
        birthday_counting = [0] * 12

        for _ in range(N):
            day, month, year = map(int, r_input().split())

            birthday_counting[month - 1] += 1
        
        print('Case #' + str(testcase) + ':')

        for ind in range(12):
            print(months[ind] + ':' + '*' * birthday_counting[ind])
        
        testcase += 1
